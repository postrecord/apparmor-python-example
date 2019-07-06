
## Python AppArmor

AppArmor interface for Python. AppArmor lets you confine processes.
More on Python: https://pythonprogramminglanguage.com

Needs sudo permission to run.
Very basic now:

    # List all profiles                                                                                                                                                    aa_status = getProfiles()

    # Get unconfined profiles                                                                                                                                              apps = getUnconfined()


