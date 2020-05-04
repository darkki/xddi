import datetime # datetime module for datetime
date_time_now = "[ " + str(datetime.datetime.now()) + " ]"
import time # time module for tictoc

from colorama import init # colorama module for colorization / ansi support
init()
from colorama import Fore,Back,Style

import os.path

import wmi
c = wmi.WMI()

class app_info:
    # version = "0.0.0-0d" # major.minor.patch-tweak / a=alpha, b=beta, rc=releasecanditate, d=development, r=release
    version = "27/4/2020|Dev" # dev version
    infoline_beta = "] xDiSKDRiVE-iNFO v0.4b by darkk! ["
    infoline = "] xD DRiVE-iNFO v" + version + " by darkk! ["
    header = infoline.center(90, "-")
    infoline2 = "] NZTi! ["
    footer = infoline2.center(90,"-")

def commafy(string, range = 3, seperator = ","): # function to add seperator to string between x number of chars
    new_string = ""
    index = 0
    mutant_string = str(string)
    for char in mutant_string[::-1]: # goes trough chars in string in reverse order and adds seperator every x chars
        index += 1
        if index % range == 0 and index == len(mutant_string):
            new_string += char
        elif index % range == 0:
            new_string += char + seperator
        else:
            new_string += char
    return_string = ""
    for char in new_string[::-1]: # reverses whole string
        return_string += char
    return(return_string)

def used_bar(percentage_used, color = True): # returns percentage used bar #TODO: Modify/create so it takes input how long bar and creates and returns that
    percentage_used = 100 - percentage_used
    if color == True:
        if percentage_used >= 0 and percentage_used <= 5:
            return("[     ]")
        elif percentage_used >= 5 and percentage_used <= 15:
            return(f"[{Fore.GREEN}.    {Style.RESET_ALL}]")
        elif percentage_used >= 15 and percentage_used <= 25:
            return(f"[{Fore.GREEN}:    {Style.RESET_ALL}]")
        elif percentage_used >= 25 and percentage_used <= 35:
            return(f"[{Fore.GREEN}:.   {Style.RESET_ALL}]")
        elif percentage_used >= 35 and percentage_used <= 45:
            return(f"[{Fore.GREEN}::   {Style.RESET_ALL}]")
        elif percentage_used >= 45 and percentage_used <= 55:
            return(f"[{Fore.YELLOW}::.  {Style.RESET_ALL}]")
        elif percentage_used >= 55 and percentage_used <= 65:
            return(f"[{Fore.YELLOW}:::  {Style.RESET_ALL}]")
        elif percentage_used >= 65 and percentage_used <= 75:
            return(f"[{Fore.YELLOW}:::. {Style.RESET_ALL}]")
        elif percentage_used >= 75 and percentage_used <= 85:
            return(f"[{Fore.YELLOW}:::: {Style.RESET_ALL}]")
        elif percentage_used >= 85 and percentage_used <= 95:
            return(f"[{Fore.RED}::::.{Style.RESET_ALL}]")
        elif percentage_used >= 95 and percentage_used <= 100:
            return(f"[{Fore.RED}:::::{Style.RESET_ALL}]")
    else:
        if percentage_used >= 0 and percentage_used <= 5:
            return("[     ]")
        elif percentage_used >= 5 and percentage_used <= 15:
            return("[.    ]")
        elif percentage_used >= 15 and percentage_used <= 25:
            return("[:    ]")
        elif percentage_used >= 25 and percentage_used <= 35:
            return("[:.   ]")
        elif percentage_used >= 35 and percentage_used <= 45:
            return("[::   ]")
        elif percentage_used >= 45 and percentage_used <= 55:
            return("[::.  ]")
        elif percentage_used >= 55 and percentage_used <= 65:
            return("[:::  ]")
        elif percentage_used >= 65 and percentage_used <= 75:
            return("[:::. ]")
        elif percentage_used >= 75 and percentage_used <= 85:
            return("[:::: ]")
        elif percentage_used >= 85 and percentage_used <= 95:
            return("[::::.]")
        elif percentage_used >= 95 and percentage_used <= 100:
            return("[:::::]")

def local_disk_drives(color = True): # function to handle local disk drives #TODO: handle every type of drives via this same function
    all_drive_space = 0
    all_space_free = 0
    volume_name_space = 14
    volume_name_fillchar = " "
    for disk in c.Win32_LogicalDisk(DriveType=3): # goes trough all logical disks
        swapfile_var = disk.Caption
        swapfile_var += "/pagefile.sys"
        windowsdir_var = disk.Caption
        windowsdir_var += "/Windows"
        flag_var = ""
        if os.path.exists(windowsdir_var) and color:
            flag_var += f"{Fore.GREEN}SYS{Style.RESET_ALL}"
        elif os.path.exists(windowsdir_var) and color == False:
            flag_var += f"SYS"
        elif os.path.isfile(swapfile_var) and color:
            flag_var += f"{Fore.CYAN}PF {Style.RESET_ALL}"
        elif os.path.isfile(swapfile_var) and color == False:
            flag_var += f"PF "
        else:
            flag_var = "   "
        letter = disk.Caption
        volume_name = disk.VolumeName.center(volume_name_space, volume_name_fillchar)
        filesystem = disk.FileSystem.center(5)
        free_space = int(disk.FreeSpace)
        free_space_kb = round(free_space // 1000, 0)
        total_space = int(disk.Size)
        total_space_kb = round(total_space // 1000, 0)
        space_used_percentage = round(free_space / total_space * 100, 1)
        space_used_percentage_print = str(space_used_percentage).rjust(4)
        # compressed = disk.Compressed
        # quotas = disk.SupportsDiskQuotas
        filebased_compression_support = disk.SupportsFileBasedCompression
        all_drive_space += total_space
        all_space_free += free_space
        free_space_kb = commafy(free_space_kb).rjust(14, " ")
        total_space_kb = commafy(total_space_kb).rjust(14)
        if color == True:
            print(f" {Style.BRIGHT}{letter}{Style.RESET_ALL} [{Style.BRIGHT}{volume_name[0:volume_name_space]}{Style.RESET_ALL}] - {free_space_kb} ({Style.BRIGHT}{space_used_percentage_print} %{Style.RESET_ALL}) / {total_space_kb} kb [{Style.BRIGHT}{filesystem[0:5]}{Style.RESET_ALL}] - [{Style.BRIGHT}{flag_var}{Style.RESET_ALL}] {used_bar(space_used_percentage)}")
        else:
            print(f" {letter} [{volume_name[0:volume_name_space]}] - {free_space_kb} ({space_used_percentage_print} %) / {total_space_kb} kb [{filesystem[0:5]}] - [{flag_var}] {used_bar(space_used_percentage)}")

def check_type(drive_type): # checks if any drives of this type exists or not
    for disk in c.Win32_LogicalDisk(DriveType=drive_type):
        if disk.Caption == None: # this line could be almost anything
            return(False) #* None is False!
        else:
            return(True)

def removable_disks(color = True): # function to handle removable disks
    all_drive_space = 0
    all_space_free = 0
    volume_name_space = 14
    volume_name_fillchar = " "
    for disk in c.Win32_LogicalDisk(DriveType=2): # goes trough all logical disks
        letter = disk.Caption
        volume_name = disk.VolumeName.center(volume_name_space, volume_name_fillchar)
        filesystem = disk.FileSystem.center(5)
        free_space = int(disk.FreeSpace)
        free_space_kb = round(free_space // 1000, 0)
        total_space = int(disk.Size)
        total_space_kb = round(total_space // 1000, 0)
        space_used_percentage = round(free_space / total_space * 100, 1)
        space_used_percentage_print = str(space_used_percentage).rjust(4)
        # compressed = disk.Compressed
        # quotas = disk.SupportsDiskQuotas
        # filebased_compression_support = disk.SupportsFileBasedCompression
        dirty_volume = disk.VolumeDirty
        all_drive_space += total_space
        all_space_free += free_space
        free_space_kb = commafy(free_space_kb).rjust(14, " ")
        total_space_kb = commafy(total_space_kb).rjust(14)
        flag_var = ""
        if dirty_volume == True and color:
            flag_var += f"{Fore.RED}DRT{Style.RESET_ALL}"
        elif dirty_volume == True and color == False:
            flag_var += f"DRT"
        else:
            flag_var += f"   "
        if color == True:
            print(f" {Style.BRIGHT}{letter}{Style.RESET_ALL} [{Style.BRIGHT}{volume_name[0:volume_name_space]}{Style.RESET_ALL}] - {free_space_kb} ({Style.BRIGHT}{space_used_percentage_print} %{Style.RESET_ALL}) / {total_space_kb} kb [{Style.BRIGHT}{filesystem[0:5]}{Style.RESET_ALL}] - [{Fore.RED}{flag_var}{Style.RESET_ALL}] {used_bar(space_used_percentage)}")
        else:
            print(f" {letter} [{volume_name[0:volume_name_space]}] - {free_space_kb} ({space_used_percentage_print} %) / {total_space_kb} kb [{filesystem[0:5]}] - [{flag_var}] {used_bar(space_used_percentage)}")

def network_drives(color = True): #function to handle network drives
    all_drive_space = 0
    all_space_free = 0
    volume_name_space = 14
    volume_name_fillchar = " "
    for disk in c.Win32_LogicalDisk(DriveType=4): # goes trough all logical disks
        letter = disk.Caption
        volume_name = disk.VolumeName.center(volume_name_space, volume_name_fillchar)
        filesystem = disk.FileSystem.center(5)
        free_space = int(disk.FreeSpace)
        free_space_kb = round(free_space // 1000, 0)
        total_space = int(disk.Size)
        total_space_kb = round(total_space // 1000, 0)
        space_used_percentage = round(free_space / total_space * 100, 1)
        space_used_percentage_print = str(space_used_percentage).rjust(4)
        # compressed = disk.Compressed
        # quotas = disk.SupportsDiskQuotas
        network_path = disk.ProviderName
        filebased_compression_support = disk.SupportsFileBasedCompression
        all_drive_space += total_space
        all_space_free += free_space
        free_space_kb = commafy(free_space_kb).rjust(14, " ")
        total_space_kb = commafy(total_space_kb).rjust(14)
        flag_var = ""
        if filebased_compression_support == True and color:
            flag_var += f"{Fore.YELLOW}R/W{Style.RESET_ALL}"
        elif filebased_compression_support == True and color == False:
            flag_var += f"R/W"
        else:
            flag_var += f"   "
        if color == True:
            print(f" {Style.BRIGHT}{letter}{Style.RESET_ALL} [{Style.BRIGHT}{volume_name[0:volume_name_space]}{Style.RESET_ALL}] - {free_space_kb} ({Style.BRIGHT}{space_used_percentage_print} %{Style.RESET_ALL}) / {total_space_kb} kb [{Style.BRIGHT}{filesystem[0:5]}{Style.RESET_ALL}] - [{Style.BRIGHT}{flag_var}{Style.RESET_ALL}] {used_bar(space_used_percentage)}")
        else:
            print(f" {letter} [{volume_name[0:volume_name_space]}] - {free_space_kb} ({space_used_percentage_print} %) / {total_space_kb} kb [{filesystem[0:5]}] - [{flag_var}] {used_bar(space_used_percentage)}")

def optical_drives(color = True): #function to handle network drives
    all_drive_space = 0
    all_space_free = 0
    volume_name_space = 14
    volume_name_fillchar = " "
    for disk in c.Win32_LogicalDisk(DriveType=5): # goes trough all logical disks
        letter = disk.Caption
        volume_name = disk.VolumeName.center(volume_name_space, volume_name_fillchar)
        filesystem = disk.FileSystem.center(5)
        free_space = int(disk.FreeSpace)
        free_space_kb = round(free_space // 1000, 0)
        total_space = int(disk.Size)
        total_space_kb = round(total_space // 1000, 0)
        space_used_percentage = round(free_space / total_space * 100, 1)
        space_used_percentage_print = str(space_used_percentage).rjust(4)
        description = str(disk.Description).rjust(17).upper()
        # compressed = disk.Compressed
        # quotas = disk.SupportsDiskQuotas
        filebased_compression_support = disk.SupportsFileBasedCompression
        all_drive_space += total_space
        all_space_free += free_space
        free_space_kb = commafy(free_space_kb).rjust(14, " ")
        total_space_kb = commafy(total_space_kb).rjust(14)
        flag_var = "   "
        if color == True:
            print(f" {Style.BRIGHT}{letter}{Style.RESET_ALL} [{Style.BRIGHT}{volume_name[0:volume_name_space]}{Style.RESET_ALL}] - {total_space_kb} ({Style.BRIGHT}--.- %{Style.RESET_ALL}) / {description} [{Style.BRIGHT}{filesystem[0:5]}{Style.RESET_ALL}] - [{Style.BRIGHT}{flag_var}{Style.RESET_ALL}] [{Style.BRIGHT}:::::{Style.RESET_ALL}]")
        else:
            print(f" {letter} [{volume_name[0:volume_name_space]}] - {total_space_kb} (--.- %) / {description} [{filesystem[0:5]}] - [{flag_var}] [:::::]")

# for os in c.Win32_OperatingSystem():
#   print(os.Caption)


# print('OS is: {0}'.format(c.Win32_OperatingSystem()[0].Caption))
# print('Disk freespace {0} - total {1}'.format(c.Win32_LogicalDisk()[0].Freespace,c.Win32_LogicalDisk()[0].Size))
# print('Total Memory: {0}'.format(c.Win32_ComputerSystem()[0].TotalPhysicalMemory))

# wql = "SELECT IPAddress FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled = 'True'"
# print('Local IP address: {0}'.format(''.join(c.query(wql)[0].IPAddress)))

# print(f"free space {c.Win32_LogicalDisk()[1].Size}")

# for disk in c.Win32_LogicalDisk():
#   print(disk)

# for disk in c.Win32_LogicalDisk():
#   print(disk.Caption)

# for disk in c.Win32_LogicalDisk(["Caption"], DriveType=3):
#   print(disk)

print(f"{Style.NORMAL}\n{app_info.header}\n{Style.RESET_ALL}")
print("local drives:")
local_disk_drives()

if check_type(2) == True: # checks if there are any removable drives, if found prints them
    print("\n" + "removable drives:")
    removable_disks()
else:
    pass

if check_type(4) == True: # checks if there are any network drives, if found prints them
    print("\n" + "network drives:")
    network_drives()
else:
    pass

if check_type(5) == True: # checks if there are any optical drives, if found prints them
    print("\n" + "optical drives:")
    optical_drives()
else:
    pass

print("\n" + app_info.footer + "\n")

#TODO: argument parsing [argparse]
#TODO: flags, network ProviderName, kb to optical size, layers / dvd/cdrom type to opticals
#TODO: if exists swapfile and windows dir!