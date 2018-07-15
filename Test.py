import sys;

utterance = str(" ");
i = 0;

triggers1 = ["power on", "boot", "bootup", "start", "startup"];
triggers2 = "office";

while utterance != "exit":
    if i is 1:
        if (any(trigger in utterance for trigger in triggers1)) and (triggers2 in utterance):
            print "Now starting up the office\n";
        else:
            print "Command not recognised\n";
    else:
        i = i + 1;
    utterance = raw_input("K2S0: ");
