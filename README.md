# SA-strexpand
Custom search command for Splunk to allow python's string expansion functionality.

## Installation
```
$ cd $SPLUNK_HOME/etc/apps
$ git clone https://github.com/sr735/SA-strexpand.git
$ $SPLUNK_HOME/bin/splunk restart
```

## Usage
This is a streaming command, so it cannot be the first command in a search as it requires existing events to append to.

### Usage without existing events
```
  | makeresults
  | strexpand <STR> <INT>
```

If value types are not valid, a NoneType value will be returned. Otherwise, value will be a string. Output field will
be called result, so be careful when naming fields in existing events to avoid overwriting them. 
