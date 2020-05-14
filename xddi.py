import datetime # datetime module for datetime
from datetime import date
date_time_now = "[ " + str(datetime.datetime.now()) + " ]"
import time # time module for tictoc

from colorama import init # colorama module for colorization / ansi support
init()
from colorama import Fore,Back,Style

import os
import os.path

import wmi
c = wmi.WMI()

import argparse

class app_info:
    # version = "0.00-0d" # major.minor|patch-tweak / a=alpha, b=beta, rc=releasecanditate, d=development, r=release
    app = "xddi"
    by = "darkki"
    version = "0.42b" # dev version #* Remember to modify parser, readme and whatnew versions too!
    # infoline_beta = "] xDiSKDRiVE-iNFO v0.4b by darkk! ["
    infoline = f"] {app} v{version} by {by} ["
    header = infoline.center(90, "-")
    infoline2 = "] xddi -h for help! ["
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
        # filebased_compression_support = disk.SupportsFileBasedCompression
        free_space_kb = commafy(free_space_kb).rjust(14, " ")
        total_space_kb = commafy(total_space_kb).rjust(14)
        if color == True:
            print(f" {Style.BRIGHT}{letter}{Style.RESET_ALL} [{Style.BRIGHT}{volume_name[0:volume_name_space]}{Style.RESET_ALL}] - {free_space_kb} ({Style.BRIGHT}{space_used_percentage_print} %{Style.RESET_ALL}) / {total_space_kb} kb [{Style.BRIGHT}{filesystem[0:5]}{Style.RESET_ALL}] - [{Style.BRIGHT}{flag_var}{Style.RESET_ALL}] {used_bar(space_used_percentage, args.mono)}")
        else:
            print(f" {letter} [{volume_name[0:volume_name_space]}] - {free_space_kb} ({space_used_percentage_print} %) / {total_space_kb} kb [{filesystem[0:5]}] - [{flag_var}] {used_bar(space_used_percentage, args.mono)}")

def check_type(drive_type): # checks if any drives of this type exists or not
    for disk in c.Win32_LogicalDisk(DriveType=drive_type):
        if disk.Caption == None: # this line could be almost anything
            return(False) #* None is False!
        else:
            return(True)

def removable_disks(color = True): # function to handle removable disks
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
        dirty_volume = disk.VolumeDirty
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
            print(f" {Style.BRIGHT}{letter}{Style.RESET_ALL} [{Style.BRIGHT}{volume_name[0:volume_name_space]}{Style.RESET_ALL}] - {free_space_kb} ({Style.BRIGHT}{space_used_percentage_print} %{Style.RESET_ALL}) / {total_space_kb} kb [{Style.BRIGHT}{filesystem[0:5]}{Style.RESET_ALL}] - [{Fore.RED}{flag_var}{Style.RESET_ALL}] {used_bar(space_used_percentage, args.mono)}")
        else:
            print(f" {letter} [{volume_name[0:volume_name_space]}] - {free_space_kb} ({space_used_percentage_print} %) / {total_space_kb} kb [{filesystem[0:5]}] - [{flag_var}] {used_bar(space_used_percentage, args.mono)}")

def network_drives(color = True, show_network_path = True): #function to handle network drives
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
        network_path = disk.ProviderName
        network_path_v2 = network_path.upper()
        # filebased_compression_support = disk.SupportsFileBasedCompression
        free_space_kb = commafy(free_space_kb).rjust(14, " ")
        total_space_kb = commafy(total_space_kb).rjust(14)
        write_test_path = letter + "/xddi_wt"
        flag_var = ""
        try:
            os.mkdir(write_test_path)
            os.rmdir(write_test_path)
        except OSError:
            if color:
                flag_var += f"{Fore.YELLOW}R{Style.RESET_ALL}/ "
            else:
                flag_var += f"R/ "
        else:
            if color:
                flag_var += f"{Fore.YELLOW}R{Style.RESET_ALL}/{Fore.YELLOW}W{Style.RESET_ALL}"
            else:
                flag_var += f"R/W"
        if color == True:
            print(f" {Style.BRIGHT}{letter}{Style.RESET_ALL} [{Style.BRIGHT}{volume_name[0:volume_name_space]}{Style.RESET_ALL}] - {free_space_kb} ({Style.BRIGHT}{space_used_percentage_print} %{Style.RESET_ALL}) / {total_space_kb} kb [{Style.BRIGHT}{filesystem[0:5]}{Style.RESET_ALL}] - [{Style.BRIGHT}{flag_var}{Style.RESET_ALL}] {used_bar(space_used_percentage, args.mono)}")
            if show_network_path:
                print(f" {Style.BRIGHT}->{Style.RESET_ALL} {network_path_v2}")
            else:
                pass
        else:
            print(f" {letter} [{volume_name[0:volume_name_space]}] - {free_space_kb} ({space_used_percentage_print} %) / {total_space_kb} kb [{filesystem[0:5]}] - [{flag_var}] {used_bar(space_used_percentage, args.mono)}")
            if show_network_path:
                print(f" -> {network_path_v2}")
            else:
                pass

def optical_drives(color = True): #function to handle network drives
    volume_name_space = 14
    volume_name_fillchar = " "
    for disk in c.Win32_LogicalDisk(DriveType=5): # goes trough all logical disks
        letter = disk.Caption
        volume_name = disk.VolumeName.center(volume_name_space, volume_name_fillchar)
        filesystem = disk.FileSystem.center(5)
        total_space = int(disk.Size)
        total_space_kb = round(total_space // 1000, 0)
        description = str(disk.Description).rjust(14).upper()
        free_space_kb = commafy(free_space_kb).rjust(14, " ")
        total_space_kb = commafy(total_space_kb).rjust(14)
        # flag_var = "R/ "
        if color == True:
            print(f" {Style.BRIGHT}{letter}{Style.RESET_ALL} [{Style.BRIGHT}{volume_name[0:volume_name_space]}{Style.RESET_ALL}] - {description} ({Style.BRIGHT}--.- %{Style.RESET_ALL}) / {total_space_kb} kb [{Style.BRIGHT}{filesystem[0:5]}{Style.RESET_ALL}] - [---] [-----]")
        else:
            print(f" {letter} [{volume_name[0:volume_name_space]}] - {description} (--.- %) / {total_space_kb} kb [{filesystem[0:5]}] - [---] [-----]")

def ram_disk_drives(color = True): # function to handle ram disk drives
    volume_name_space = 14
    volume_name_fillchar = " "
    for disk in c.Win32_LogicalDisk(DriveType=6): # goes trough all logical disks
        letter = disk.Caption
        volume_name = disk.VolumeName.center(volume_name_space, volume_name_fillchar)
        filesystem = disk.FileSystem.center(5)
        free_space = int(disk.FreeSpace)
        free_space_kb = round(free_space // 1000, 0)
        total_space = int(disk.Size)
        total_space_kb = round(total_space // 1000, 0)
        space_used_percentage = round(free_space / total_space * 100, 1)
        space_used_percentage_print = str(space_used_percentage).rjust(4)
        free_space_kb = commafy(free_space_kb).rjust(14, " ")
        total_space_kb = commafy(total_space_kb).rjust(14)
        if color == True:
            print(f" {Style.BRIGHT}{letter}{Style.RESET_ALL} [{Style.BRIGHT}{volume_name[0:volume_name_space]}{Style.RESET_ALL}] - {free_space_kb} ({Style.BRIGHT}{space_used_percentage_print} %{Style.RESET_ALL}) / {total_space_kb} kb [{Style.BRIGHT}{filesystem[0:5]}{Style.RESET_ALL}] - [---] {used_bar(space_used_percentage, args.mono)}")
        else:
            print(f" {letter} [{volume_name[0:volume_name_space]}] - {free_space_kb} ({space_used_percentage_print} %) / {total_space_kb} kb [{filesystem[0:5]}] - [---] {used_bar(space_used_percentage, args.mono)}")

def totals(color, no_memory): # prints total drive and memory info
    all_space_total = 0
    all_space_free = 0
    for disk in c.Win32_LogicalDisk(DriveType=3):
        free_space = int(disk.FreeSpace)
        all_space_free += round(free_space // 1000, 0)
        total_space = int(disk.Size)
        all_space_total += round(total_space // 1000, 0)
    if check_type(2) == True:
        for disk in c.Win32_LogicalDisk(DriveType=2):
            free_space = int(disk.FreeSpace)
            all_space_free += round(free_space // 1000, 0)
            total_space = int(disk.Size)
            all_space_total += round(total_space // 1000, 0)
    else:
        pass
    if check_type(4) == True:
        for disk in c.Win32_LogicalDisk(DriveType=4):
            free_space = int(disk.FreeSpace)
            all_space_free += round(free_space // 1000, 0)
            total_space = int(disk.Size)
            all_space_total += round(total_space // 1000, 0)
    else:
        pass
    if no_memory:
        all_used_percentage = round(all_space_free / all_space_total * 100, 1)
        all_used_percentage = str(all_used_percentage).rjust(24)
        all_space_used = all_space_total - all_space_free
        all_space_total = commafy(all_space_total).rjust(24)
        all_space_used = commafy(all_space_used).rjust(22)
        all_space_free = commafy(all_space_free).rjust(22)
    else: #? querying memory creates major slowdown, is there way to speed things up?
        for cs in c.Win32_ComputerSystem():
            memory_total = int(cs.TotalPhysicalMemory)
        for perfos_mem in c.Win32_PerfFormattedData_PerfOS_Memory():
            memory_free = int(perfos_mem.AvailableBytes)
        all_used_percentage = round(all_space_free / all_space_total * 100, 1)
        all_used_percentage = str(all_used_percentage).rjust(23)
        all_space_used = all_space_total - all_space_free
        all_space_total = commafy(all_space_total).rjust(23)
        all_space_used = commafy(all_space_used).rjust(23)
        all_space_free = commafy(all_space_free).rjust(23)
        memory_total = round(memory_total // 1000, 0)
        memory_free = round(memory_free // 1000, 0)
        memory_used = memory_total - memory_free
        memory_percentage = round(memory_free / memory_total * 100, 1)
        memory_percentage = str(memory_percentage).rjust(15)
        memory_total = commafy(memory_total).rjust(15)
        memory_free = commafy(memory_free).rjust(15)
        memory_used = commafy(memory_used).rjust(15)
    if color == True and no_memory == False:
        print()
        print(f" total drivespace : {Style.BRIGHT}{all_space_total}{Style.RESET_ALL} kb {Style.BRIGHT}-{Style.RESET_ALL}   total memory      : {Style.BRIGHT}{memory_total}{Style.RESET_ALL} kb")
        print(f" total space used : {Style.BRIGHT}{all_space_used}{Style.RESET_ALL} kb {Style.BRIGHT}-{Style.RESET_ALL}   total memory used : {Style.BRIGHT}{memory_used}{Style.RESET_ALL} kb")
        print(f" total space free : {Style.BRIGHT}{all_space_free}{Style.RESET_ALL} kb {Style.BRIGHT}-{Style.RESET_ALL}   total memory free : {Style.BRIGHT}{memory_free}{Style.RESET_ALL} kb")
        print(f" percentage free  : {Style.BRIGHT}{all_used_percentage}{Style.RESET_ALL} %  {Style.BRIGHT}-{Style.RESET_ALL}   percentage free   : {Style.BRIGHT}{memory_percentage}{Style.RESET_ALL} %")
    elif color == False and no_memory == False:
        print()
        print(f" total drivespace : {all_space_total} kb -   total memory      : {memory_total} kb")
        print(f" total space used : {all_space_used} kb -   total memory used : {memory_used} kb")
        print(f" total space free : {all_space_free} kb -   total memory free : {memory_free} kb")
        print(f" percentage free  : {all_used_percentage} %  -   percentage free   : {memory_percentage} %")
    elif color == True and no_memory == True:
        print()
        print(f" total drivespace: {Style.BRIGHT}{all_space_total}{Style.RESET_ALL} kb {Style.BRIGHT}-{Style.RESET_ALL}   total used : {Style.BRIGHT}{all_space_used}{Style.RESET_ALL} kb")
        print(f" percentage free : {Style.BRIGHT}{all_used_percentage}{Style.RESET_ALL} %  {Style.BRIGHT}-{Style.RESET_ALL}   total free : {Style.BRIGHT}{all_space_free}{Style.RESET_ALL} kb")
    elif color == False and no_memory == True:
        print()
        print(f" total drivespace: {all_space_total} kb -   total used : {all_space_used} kb")
        print(f" percentage free : {all_used_percentage} %  -   total free : {all_space_free} kb")

parser = argparse.ArgumentParser(prog="xddi", description="displays your local, network, removable and optical drives with usage and other useful information")
parser.add_argument("-v", "--version", action="version", version="%(prog)s v0.42b")
parser.add_argument("-m", "--mono", help="output in monochrome (no colors)", action="store_false")
parser.add_argument("-np", "--nopath", help="does not display network path", action="store_false")
parser.add_argument("-nt", "--nototals", help="does not display drive/memory totals (also boosts speed)", action="store_true")
parser.add_argument("-nm", "--nomemory", help="does not display memory totals (also boosts speed)", action="store_true")
args = parser.parse_args()

tic = time.time()

print(f"\n{app_info.header}\n")
print("local drives:")
local_disk_drives(args.mono)

if check_type(2) == True: # checks if there are any removable drives, if found prints them
    print("\n" + "removable drives:")
    removable_disks(args.mono)
else:
    pass

if check_type(4) == True: # checks if there are any network drives, if found prints them
    print("\n" + "network drives:")
    network_drives(args.mono, args.nopath)
else:
    pass

if check_type(5) == True: # checks if there are any optical drives, if found prints them
    print("\n" + "optical drives:")
    optical_drives(args.mono)
else:
    pass

if check_type(6) == True: # checks if there are any optical drives, if found prints them
    print("\n" + "ram disk drives:")
    ram_disk_drives(args.mono)
else:
    pass

if args.nototals:
    pass
else:
    totals(args.mono, args.nomemory)

toc = time.time()
tictoc = round(toc - tic, 2)
infoline2 = f"] xddi -h for help! ({tictoc}s) ["
footer = infoline2.center(90,"-")

print("\n" + footer + "\n")