# check_pi-hole
This is a Nagios plugin to monitor Pi-Hole.

With this plugin you can monitor Pi-Hole for the following values:
- total queries
- blocked today
- percent today
- unique domains
- queries forwarded
- queries cached
- unique_clients

Usage:

check_pi-hole.py -H <host> <options> <parameter>

Command line options:
  
  -h,  --help           'Displays this message', action='help'
  -t,  --timeout        'timeout', default=500, type=int
  -w,  --warning        'warning threshold', default=None
  -c,  --critical       'critical threshold', default=None
  -H,  --hostname       'Hostname', default=ip
  -T,  --token          'Token', default=None
  -v,  --verbose        'Verbose mode', action='store_true'
  
  'parameter'    'total_queries', 'blocked_today', 'pct_today', 'unique_domains', 'queries_forwarded', 'queries_cached', 'unique_clients'      
  


Thx to AngularSpecter and Fliegema for the beautiful work.

Original Source Code from here: https://pastebin.com/awpqZgJg by reddit user: u/AngularSpecter.

Further developed from here: https://pastebin.com/2Ua3JeTr by reddit user: u/Fliegema.
