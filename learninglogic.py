import sys;

utterance = str(" ");
i = 0;

#TODO Move commands to the MyCroft file format
triggers1 = ["power on", "boot", "bootup", "start", "startup"];
triggers2 = "office";

#TODO Create config file and initalize list of MAC addresses from file

#TODO Remove command loop, for testing only
while utterance != "exit":
    if i is 1:
        if (any(trigger in utterance for trigger in triggers1)) and (triggers2 in utterance):
            print ("Now starting up the office\n");
            #TODO Add logic to send WOL packet to Specific MAC address on network
        else:
            print ("Command not recognised\n");
    else:
        i = i + 1;
    utterance = input("K2S0: ");
