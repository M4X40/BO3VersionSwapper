import os
import subprocess
import shutil

def cls():
  subprocess.run('cls', shell=True)
def pause():
  subprocess.run('pause', shell=True)

sizes = {
  "9084453472036406216": 143134192,
  "7651791086710252932": 105994224,
  "8824612235115253119": 106059256,
}

def manualSelect():
  gamePath = ""
  while True:
    cls()
    print(f"""
    --=[   Black Ops 3 || Version Swapper   ]=--
    ----=[          Made by M4X4          ]=----
    
    """)
    gamePath = input("Enter current BO3 install directory  >> ")
    if os.path.isdir(gamePath):
      break
  while True:
    cls()
    exePath = os.path.join(gamePath, "BlackOps3.exe")
    exeSize = os.path.getsize(exePath)
    AVersionSelector = " <- Current" if exeSize == 143134192 else ""
    BVersionSelector = " <- Current" if exeSize == 105994224 else ""
    CVersionSelector = " <- Current" if exeSize == 106059256 else ""
    print(f"""
    --=[   Black Ops 3 || Version Swapper   ]=--
    ----=[          Made by M4X4          ]=----

    [a] March 3, 2023 (100.2.2.7.105.0) (ManifestID 9084453472036406216) {AVersionSelector}
    [b] February 19, 2026 (100.2.2.7.127.0) (ManifestID 7651791086710252932) [RECOMMENDED] {BVersionSelector}
    [c] September 10, 2026 (100.2.2.7.129.0) (ManifestID 8824612235115253119) {CVersionSelector}
    """)
    selection = input("Select version to swap to  >> ")
    try:
      manifest = ""
      if selection.lower() == "a":
        manifest = "9084453472036406216"
      elif selection.lower() == "b":
        manifest = "7651791086710252932"
      elif selection.lower() == "c":
        manifest = "8824612235115253119"
      else:
        raise SyntaxError("Answer needs to be 'a', 'b', or 'c'")

      subprocess.run(f"echo download_depot 311210 311211 {manifest} | clip".split(), shell=True)
      print("Copied command to clipboard!")
      print("Reopening steam with console")
      subprocess.run("taskkill /F /IM steam.exe".split(), capture_output=True)
      os.startfile("steam://open/console")
      # Assume default install path
      path = "C:\\Program Files (x86)\\Steam\\steamapps\\content\\app_311210\\depot_311211\\"
      installPath = os.path.join(path, "BlackOps3.exe")
      try:
        os.remove(installPath)
      except:
        pass
      print("In the console window, paste the copied command into the command bar at the bottom.\n\nWaiting for BlackOps3.exe to be downloaded...")
      isFound = False
      while not isFound:
        isFound = os.path.isfile(installPath) and os.path.getsize(installPath) == sizes[manifest]
      while True:
        try:
          shutil.copy(os.path.join(path, "BlackOps3.exe"), gamePath)
          break
        except:
          continue

    except Exception as e:
      print(f"ERR! {e}")
      pause()

def manual():
  while True:
    cls()
    manualSelect()

def modeSelect():
  while True:
    cls()
    print(f"""
      --=[   Black Ops 3 || Version Swapper   ]=--
      ----=[          Made by M4X4          ]=----

      [a] Automatic mode (W.I.P)
      [b] Manual mode
      """)
    mode = input("Select mode  >> ")
    if mode.lower() == "b":
      manual()

modeSelect()