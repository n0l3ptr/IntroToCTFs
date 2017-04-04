# N0l3ptr r2 Cheat Sheet

We find that r2's documentation can be quite old and uninformative so we decided to make our own cheat sheet. Some of this we picked up from the docs, other cheat sheets, or old CTF write-ups. Let us know if anything is out of date!

## Contents
|Topic                              |Program/File|Index|
|-----------------------------------|------------|-----|
|Downloading/Installing             |            |1    |
|Starting r2                        |radare2     |2    |
|Binary Information Extraction      |rabin2      |3    |
|Run binaries in exotic environments|rarun2      |4    |
|Project files                      |radare2     |5    |
|Custom Config file                 |~/.radare2rc|6    |
|Shellcode generation               |ragg2       |7    |
|Diff files                         |radiff2     |8    |
|TODO / Wish list                   |            |Last |


##1: Downloading/Installing

`wget https://github.com/radare/radare2 #` in order to download and follow instructions there (sys/install.sh for global install, sys/user.sh for local)


##2: Starting r2 (radare2)

`r2 filename` will start and open radare2 with the specified binary file.
radare2 can also be started while specifying many different arguments on the command-line. Bellow we cover some the flags we find to be most useful when starting radare2.

`Usage: r2 [-flags] filename`

|Functionality     |Flag|Comment|
|------------------|----|-------|
|Analyze Binary    |-A  |-AA is recommended; Includes developmental analyses features.
|Debug mode        |-d  |       |
|Write mode        |-w  |       |
|Open project      |-p [proj]|  |
|Sandbox mode       |-S  |*SECURITY OF SANDBOX NOT VERIFIED BY n0l3ptr*|


##3: Binary Information Extraction (rabin2)

rabin2 is a tool for examining/extracting properties and information from binary files (e.g. ELF). rabin2 is installed as part of the core of r2 so there is no need to install rabin2, if you already have r2. 

`Usage: rabin2 [-flags] filename`

|Function                |Flag|Comparable Functionality     |Comment|
|------------------------|----|-----------------------------|-------|
|Binary Info             |-I  |file, checksec               |check relro = rabin2 -k 'info/*' file \| grep relro       |
|Dump raw strings        |-zzz|strings                      |More secure than strings|
|Show Entry-point        |-e  |readelf -h file \| grep Entry|       | 
|Address of main symbol  |-M  |readelf -a file \| grep main |       |
|Linked libraries        |-l  |ldd                          |       |
|Library imported symbols|-i  |objdump -T file              |       |
|Relocations             |-R  |readelf -r file              |readelf -r file may show version numbers as well       |


##4: Run binaries in exotic environments (rarun2)

rarun2 also comes along with the r2 core and allows us to locally host/run binaries. Below gives the basic usage of rarun2 to be able to setup interaction with the binary remotely. Rarun2 has many more paraters that can be used to set up a unique environment to run the binary.

`Usage: rarun2 [parameters=values] program=/file`

|Function                |Flag|Comparable Functionality     |Comment|
|------------------------|----|-----------------------------|-------|
|Binary to run           |program=/file| ./file | If no other parameters the binary will simply run|
|Port to listen on | listen=8080 | | Binary can be interacted with at designated port|  
|Pass args to binary| arg1=Value | ./file value |

##5: Project Files (radare2)

_Disclaimer: Projects files are highly subject to change but here is the current state on March 14th 2017. The feature is still under high work in progress._

radare2 Project files are especially useful to save your work for later use, share your work with other, and scripting for radare2. 

`Usage: Start r2 with the desired binary: 'r2 filename' Once in the radare2 you can use the commands below: `

|Functionality|Command  |Comment|
|-------------|---------|-------|
|Create/Save  |Ps [project name]|Saves the current radare2 session or creates a new project. ~/.config/radare2/projects/|
|Open         |Po name  |Open a saved project|
|List projects|Pl       |List all saved projects| 
|Show project notes|Pn | Displays the project notes file:~/.config/radare2/projects/myproj/notes.txt| 
|Edit project notes|Pn -|Opens the project notes file in vim| 

##6: Custom Configuration File (~/.radare2rc)

Each line in the ~/.radare2rc file will be interpreted at the start of each session. 


##7: Shellcode Generator (ragg2)

ragg2 is yet another tool that comes in the core of radare2. ragg2 allows us to compile tiny binaries, most useful for use to generate shellcode.

`Usage: ragg2 [-flags]`

|Functionality   |Flag                  |Comment|
|----------------|----------------------|-------|
|Architecture    |-a [x86/arm]          |       |
|Register Size   |-b [32/64]            |       |
|Kernel          |-k [windows/linux/osx]|       |
|Format          |-f [raw/pe/elf/mach0] |       |
|Shellcode       |-i [exec]             |       |
|Execute         |-x                    |       |

Example shellcode generation for a x86-64 Linux machine.
`$ ragg2 -a x86 -b 64 -k linux -i exec`

##8: Diff Files






## TODO / Wish List
* r2 -S : Sandbox mode : Secure? Uses?
* radiff2
* Custom config file
* Visual Disassembly 
* Disassembly
* debugging





