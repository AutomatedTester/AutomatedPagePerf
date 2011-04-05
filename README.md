# Overview #

This is a mechanism to record the client-side performance using Python and Selenium. 
This Framework gives you a way to get HAR files of the traffic for the page.

## Example ##

    >>> from pageperfdriver import PagePerfDriver
    >>> p=PagePerfDriver()
    >>> p.get("http://www.theautomatedtester.co.uk")
    >>> p.get("http://example.com")
    >>> p.har_directory
    '/tmp/tmpA5hncX/firebug/netexport/logs'

### Note ###
Unfortunately this only works in Firefox 3.6
    
