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
<br>

### Usage:

```
./check_pi-hole.py -H <host> <options> <parameter>
```
<br>

### Command line options:
  
  ```
  -h,  --help           'Displays this message', action='help'
  -t,  --timeout        'timeout', default=500, type=int
  -w,  --warning        'warning threshold', default=None
  -c,  --critical       'critical threshold', default=None
  -H,  --hostname       'Hostname', default=ip
  -T,  --token          'Token', default=None
  -v,  --verbose        'Verbose mode', action='store_true'
  ```
<br>
  
### Parameter:
  ```
  'total_queries', 'blocked_today', 'pct_today', 'unique_domains', 'queries_forwarded', 'queries_cached', 'unique_clients'
  ```
<br>
 
 ### Example:

  ```
  ./check_pi-hole.py -H 1.2.3.4 -T 9ee7a70c635b4c31a7bc3dafc370adf4e8e785d03d8d069e253fd39db76b0e39 -w 80 -c 90 pct_today
  ```
<br>
<br>
 
 
You can find your Pi-Hole Token (Api key) in /etc/pihole/setupVars.conf. It is labeled as WEBPASSWORD.
<br>
<br>

 
Thx to AngularSpecter and Fliegema for the beautiful work.
<br>
 
Original Source Code from here: https://pastebin.com/awpqZgJg by reddit user: [AngularSpecter](https://pastebin.com/u/angularspecter).
<br>
 
Further developed from here: https://pastebin.com/2Ua3JeTr by reddit user: [Fliegema](https://pastebin.com/u/fliegema).
<br>
