#!/usr/bin/python3

import sys, base64, re, urllib.request
import argparse, json

ip = '10.8.1.10'
url = '/admin/api.php?summaryRaw&auth='

#parse command line options
parser = argparse.ArgumentParser(description = 'Check Status of PIHOLE Ad blocker' )
#parser.add_argument('-h', '--help',     help='Displays this message', action='help')
parser.add_argument('-t', '--timeout',  help='timeout', default=500, type=int )
parser.add_argument('-w', '--warning',  help='warning threshold', default=None )
parser.add_argument('-c', '--critical', help='critical threshold', default=None )
parser.add_argument('-H', '--hostname', help='Hostname', default=ip )
parser.add_argument('-T', '--token',    help='Token', default=None )
parser.add_argument('-v', '--verbose' , help='Verbose mode', action='store_true')
parser.add_argument('parameter' ,       help='parameter to check', choices=['total_queries', 'blocked_today', 'pct_today', 'unique_domains', 'queries_forwarded', 'queries_cached', 'unique_clients'])
args = parser.parse_args()


status_url = 'http://' + args.hostname + url + args.token

try:
  request = urllib.request.urlopen( status_url )
  content  = request.read()
  decoded  = json.loads( content )
except Exception:
  print ("Error contacting server")
  raise
  sys.exit(3)

################################################################
def check_range( value, rng ):
  if not rng: return False

  value = float( value )
  #check the range format
  if rng.find(':') == -1:
    rng_val = rng.replace(':','')
    rng_val = int( rng.strip() )
    return (value <0) | (value>rng_val)

  m = re.search('([\~@]?)(\d*):(\d*)', rng )

  lower_bound = float(m.group(2)) if m.group(2) else -1* float('inf')
  upper_bound = float(m.group(3)) if m.group(3) else     float('inf')
  inclusive   = True if m.group(1) and m.group(1) == '@' else False

  in_range = ( value >= lower_bound ) & ( value <= upper_bound )
  return in_range if inclusive else not in_range

#############################################################
def process_result( name, value, units, crit, warn, rng ):

  should_warn = check_range( value, warn )
  should_crit = check_range( value, crit )

  status = 'OK'
  if should_warn : status = 'WARNING'
  if should_crit : status = 'CRITICAL'

  print ('{0}: {1} = {2} | {1}={2}{3};{4};{5};{6};{7}'.format( status, name, value, units, warn, crit, rng[0], rng[1] ))

  if should_crit : sys.exit(2)
  if should_warn : sys.exit(1)
  sys.exit(0)

############################################
# parse the content

#['total_queries', 'blocked_today', 'pct_today', 'unique_domains', 'queries_forwarded', 'queries_cached', 'unique_clients'])

if args.parameter == 'total_queries':
  process_result( 'Total_queries', decoded['dns_queries_today'], '', args.critical, args.warning, [0, 65535] )

if args.parameter == 'blocked_today':
  process_result( 'Total_queries', decoded['ads_blocked_today'], '', args.critical, args.warning, [0, 65535] )

if args.parameter == 'pct_today':
  process_result( 'Total_queries', decoded['ads_percentage_today'], '%', args.critical, args.warning, [0, 100] )

if args.parameter == 'unique_domains':
  process_result( 'Unique_domains', decoded['unique_domains'], '', args.critical, args.warning, [0, 65535] )

if args.parameter == 'queries_forwarded':
  process_result( 'Queries_forwarded', decoded['queries_forwarded'], '', args.critical, args.warning, [0, 65535] )

if args.parameter == 'queries_cached':
  process_result( 'Queries_cached', decoded['queries_cached'], '', args.critical, args.warning, [0, 65535] )

if args.parameter == 'unique_clients':
  process_result( 'Unique_clients', decoded['unique_clients'], '', args.critical, args.warning, [0, 100] )
