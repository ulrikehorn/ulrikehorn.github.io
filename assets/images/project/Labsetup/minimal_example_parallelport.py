import parallel
import time

# settings
num_trials = 10
# how long the stimulus is programmed in milliseconds:
stim_dur = 200
# how long the inter-stimulus interval (ISI) is programmed in milliseconds:
isi_dur = 1000
# how long the trigger needs to be (to be detected by the device) in milliseconds:
trigger_dur = 10

# parallel port for device (here first port)
p_out = parallel.Parallel(port=0)
p_out.setData(0)

for i in range(num_trials):
    stim_given = False
    trial_start = time.time()
    while (time.time() - trial_start) <= (stim_dur / 1000):
        if not stim_given:
            while time.time() - trial_start <= trigger_dur / 1000:
                # sets pin 6 high, count from back, starts at 2
                # Could add more outputs here through extra pins (parallel ports with multi output)
                p_out.setData(int("00010000", 2))  
            # set all pins low:
            p_out.setData(0)
            print('Trial ' + str(i + 1))
            stim_given = True
    
    # wait for the inter-stimulus interval (ISI)
    time.sleep(isi_dur / 1000)