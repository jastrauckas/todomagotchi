import time
now = time.localtime()
hour1 = now.tm_hour 
hour = 10*hour1/24
#Creates an increasing value of hour as time pases so as to deplete the values linearly over time


worki= 10
schooli = 10
recreationi = 10
resti = 10
healthi = 10
#setting initial values to 10. Maybe in the future we can make a way to make yesterday's shortcomings push over to the next day's?

ha = 0 
wa = 0
reca = 0
reshours = 0 #Eventually hours of rest*some constant...maybe 2 (8 hours of rest vs 16 hours of awake to maintain the value of 10)
sa = 0
#these will eventually be replaced with increasing values as tasks are completed

health = healthi - hour + ha
work = worki - hour + wa
school = schooli - hour + sa
recreation = recreationi - hour + reca
#the value of each value over time is the initial value of 10, minus that linear time value, plus the task value
rest = resti - hour + reshours

if recreation < 4: recrestatus= 'All work and no play makes TodoMagotchi a dull boy'
#if we want to make a high value status, I've included them in comments underneath:
#elif recreation > 8: recrestatus = 'TodoMagotchi works hard, and TodoMagotchi plays hard.'

if health < 4: healthstatus= 'TodoMagotchi has died of dystentary.'
#elif heath > 8: healthstatus = 'TodoMagotchi is fighting fit! No seriously, who wants to take him?'

if rest < 4: reststatus= 'TodoMagotchi has been walking into walls for the last', now.tm_min + 5, 'minutes. It might be time for a nap. Or a red bull. But probably a nap.'

if school < 4: schoolstatus= 'TodoMagotchi is starting to question evolution.'
#elif school > 8: schoolstatus = 'TodoMagotchi understands Special Relativity! ...he\'s pretty sure he does, anyway.'

if work < 4: workstatus='TodoMagotchi has started marathoning Buffy the Vampire Slayer on Netflix. Ordinarily this would be awesome, but he needs to do work!'
#elif work > 8: workstatus = 'TodoMagotchi is totally getting a raise next quarter!'

