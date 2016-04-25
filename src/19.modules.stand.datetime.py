#!/usr/bin/env python
# coding: UTF-8

print('Hello World!')

import time, datetime
'''
    asctime(...)
        asctime([tuple]) -> string
        
        Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
        When the time tuple is not present, current time as returned by localtime()
        is used.
    
    clock(...)
        clock() -> floating point number
        
        Return the CPU time or real time since the start of the process or since
        the first call to clock().  This has as much precision as the system
        records.
    
    ctime(...)
        ctime(seconds) -> string
        
        Convert a time in seconds since the Epoch to a string in local time.
        This is equivalent to asctime(localtime(seconds)). When the time tuple is
        not present, current time as returned by localtime() is used.
    
    get_clock_info(...)
        get_clock_info(name: str) -> dict
        
        Get information of the specified clock.
    
    gmtime(...)
        gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                               tm_sec, tm_wday, tm_yday, tm_isdst)
        
        Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
        GMT).  When 'seconds' is not passed in, convert the current time instead.
        
        If the platform supports the tm_gmtoff and tm_zone, they are available as
        attributes only.
    
    localtime(...)
        localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                                  tm_sec,tm_wday,tm_yday,tm_isdst)
        
        Convert seconds since the Epoch to a time tuple expressing local time.
        When 'seconds' is not passed in, convert the current time instead.
    
    mktime(...)
        mktime(tuple) -> floating point number
        
        Convert a time tuple in local time to seconds since the Epoch.
        Note that mktime(gmtime(0)) will not generally return zero for most
        time zones; instead the returned value will either be equal to that
        of the timezone or altzone attributes on the time module.
    
    monotonic(...)
        monotonic() -> float
        
        Monotonic clock, cannot go backward.
    
    perf_counter(...)
        perf_counter() -> float
        
        Performance counter for benchmarking.
    
    process_time(...)
        process_time() -> float
        
        Process time for profiling: sum of the kernel and user-space CPU time.
    
    sleep(...)
        sleep(seconds)
        
        Delay execution for a given number of seconds.  The argument may be
        a floating point number for subsecond precision.
    
    strftime(...)
        strftime(format[, tuple]) -> string
        
        Convert a time tuple to a string according to a format specification.
        See the library reference manual for formatting codes. When the time tuple
        is not present, current time as returned by localtime() is used.
        
        Commonly used format codes:
        
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
    
    strptime(...)
        strptime(string, format) -> struct_time
        
        Parse a string to a time tuple according to a format specification.
        See the library reference manual for formatting codes (same as
        strftime()).
        
        Commonly used format codes:
        
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
    
    time(...)
        time() -> floating point number
        
        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.
'''

print(time.time())   # wall clock time, unit: second
print(time.clock())  # processor clock time, unit: second

print('start')
time.sleep(2)     # sleep for 10 seconds
print('wake up')

#time包还定义了struct_time对象。
#该对象实际上是将挂钟时间转换为年、月、日、时、分、秒……等日期信息，存储在该对象的各个属性中(tm_year, tm_mon, tm_mday...)。
#下面方法可以将挂钟时间转换为struct_time对象:
print(time.gmtime())      # 返回struct_time格式的UTC时间
print(time.localtime())   # 返回struct_time格式的当地时间, 当地时区根据系统环境决定。
print(time.mktime(time.gmtime()))    # 将struct_time格式转换成wall clock time

t      = datetime.datetime(2012,9,3,21,30)
t_next = datetime.datetime(2012,9,5,23,30)
delta1 = datetime.timedelta(seconds = 600)
delta2 = datetime.timedelta(weeks = 3)
print(t + delta1)
print(t + delta2)
print(t_next - t)
print(t > t_next)


format = "output-%Y-%m-%d-%H%M%S.txt" 
str    = "output-1997-12-23-030000.txt" 
t_format      = datetime.datetime.strptime(str, format)  #from datetime import datetime
#t_format      = t_next.strptime(str, format)
print(t_format)
print(t_next.strftime(format))

input('Please enter a code to quit:')



 
 