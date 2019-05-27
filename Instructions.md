Vorbereitungen zur Übung Nr. 7 "Tensorflow: Einführung"
===

_Übung zur Gastvorlesung von Wolfgang Giersche (Zühlke) im Modul Data Analytics (M_DatAna), Bachelor Informatik, HSR Hochschule für Technik Rapperswil, FS 2019 (Prof. Stefan Keller und Raphael Das Gupta)_

## Freiwillig: Default-Browser anpassen (Windows)

Microsoft Edge stellt die JupyterLab-Oberfläche nicht richtig dar.
Falls auf Ihrem System Edge als Standard-Browser eingestellt ist,
können Sie das in den Windows-Einstellungen
unter "System" > "Default apps" ändern.
So kann Jupyter gleich einen passenden Browser starten.

Sowohl mit Firefox als auch mit Chrome funktioniert JupyterLab gut.

## Freiwillig: Installation von Git

Sie können die Dateien für die Übung als Zip-Archiv herunterladen oder das Repository mit Git auf ihren eigenen Computer clonen.

### Git-Installation auf Windows & OS X:

Laden Sie den Installer von <https://git-scm.com/downloads> herunter.

### Git-Installation auf Linux

Anleitungen für die Installation
über die Paket-Manager diverser Linux-Distributionen
finden sie unter <https://git-scm.com/download/linux>.


## Übungs-Dateien beziehen

### Variante Git:

Starten Sie die Kommandozeile (= "Terminal" = "Konsole")
bzw. auf Windows die Git-Bash
(nach der Git-Installation im Windows-Start-Menü verfügbar)
und führen Sie folgenden Befehl aus:

```bash
git clone https://github.com/smurve/HSR2019.git
```

### Variante Zip-Archiv:

Laden Sie <https://github.com/smurve/HSR2019/archive/master.zip> herunter
und entpacken Sie den Inhalt.


## Installation der benötigten Software

Für die Übung Nr. 7 vom Mittwoch, 4. April 2019, benötigen Sie Jupyter Lab mit Python, NumPy, TensorFlow und einige Python-Libraries. Bitte nehmen Sie die Installation wenn möglich bereits vorher vor.

Es gibt folgende drei Varianten zur Installation:

* A: (empfohlen) **Lokale Python-Installation**, Rest in Python "virtualenv"
* B: (falls A nicht klappt) **lokaler Docker-Container**
* C: (falls A & B nicht gehen) **"Binder"** im Web

### Variante A: Lokale Python-Installation (empfohlen)

:::info
#### TODO: Windows-Anleitung überarbeiten
- Anaconda anstatt "normale" Python-Istallation?
- Windows Subsystem for Linux verwenden?
:::

1. Installieren Sie **Python** (wenn möglich **Python 3**).  
   Falls Sie eine Anleitung dazu benötigen, finden Sie eine unter <https://tutorial.djangogirls.org/de/python_installation/>.[^ausklappen]
2. Erstellen Sie ein **Python "virtualenv"**.  
   Eine Anleitung und Erleuterungen dazu finden Sie unter <https://tutorial.djangogirls.org/de/installation/#virtuelle-umgebung/>.[^ausklappen][^kein-django]
3. Aktivieren Sie **das "virtualenv**"  
   Eine Anleitung dazu finden Sie unter <https://tutorial.djangogirls.org/de/installation/#mit-der-virtuellen-umgebung-arbeiten>.[^ausklappen][^kein-django]
4. Erstellen Sie im aktuellen Verzeichnis eine **Plaintext-Datei namens `requirements.txt`** mit folgendem Inhalt:
   ```
   tensorflow>1.8,<1.14
   tensorflow_transform
   jupyterlab
   numpy
   matplotlib
   pandas
   seaborn
   ```
5. Installieren Sie im Terminal, in dem das "virtualenv" aktiv ist[^venv], die in der Datei `requirements.txt` spezifizierte Python-Software wie folgt:
   ```bash
   pip install -r requirements.txt
   ```

[^ausklappen]: Beachten Sie, dass dort die Betriebssystem-abhängigen Schritte jener Anleitung der Übersicht halber erst aufgeklappt werden müssen.
[^kein-django]: Nur diesen einen Abschnitt verwenden, da er Teil einer grössen Anleitung für etwas anderes ist. Django müssen Sie für die Übung nicht installieren.
[^venv]: Das können Sie an der Beschriftung `(myvenv)` am Anfang der Prompt-Zeile erkennen. Falls das in ihrem Terminal fehlt, aktivieren Sie es erneut.

Achten Sie darauf, ob Fehlermeldungen ausgegeben wurden. Nach erfolgter Installation können Sie ihr Setup wie folgt testen:

1. Starten Sie aus dem Terminal, in dem das "virtualenv" aktiv ist[^venv], Jupyter Lab:
   ```bash
   jupyter lab
   ```
   Das Ergebnis sollte so aussehen:  
   ![](https://md.coredump.ch/uploads/upload_3c1d6bc77646c035b02cd38bd981220a.png)
2. Falls dadurch kein Browser geöffnet wurde, oder falls die Jupyter-Lab-Oberfläche darin nicht korrekt dargestellt wird (z.B. in Internet Explorer oder Edge) öffnen sie die im Terminal angezeigte URL in Firefox oder Chrome.
3. Starten Sie ein Python-Notebook durch den entsprechenden Button.
4. Geben Sie folgenden Python-Code in die oberste Notebook-Zelle ein:
   ```python
   from __future__ import (absolute_import, division, print_function)
   
   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt

   import tensorflow as tf
   import seaborn as sns
   ```
5. Führen Sie die Zelle mit <kbd>⇧ Shift</kbd>+<kbd>↵ Enter</kbd> oder mit dem Run-Knopf (▶) aus.  
   Falls das zu keiner Fehlermeldung führt, sollte alles funktioniert haben.

### Variante B: Lokaler Docker-Container

(Alternative, falls Variante A nicht funktioniert).

:::info
:bulb: Hierfür muss **Docker bereits installiert** sein.
:::

Starten Sie wie folgt einen flüchtigen Docker-Container basierend auf dem Docker-Image `jupyter/tensorflow-notebook` (dieses wird hierdurch falls notwendig automatisch heruntergeladen):

Bash (OS X, Linux, oder auf Windows Git Bash oder MinGW):
```bash
docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work jupyter/tensorflow-notebook
```

Windows CMD:
```cmd
docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "%CD%":/home/jovyan/work jupyter/tensorflow-notebook
```

Warten Sie, bis der Container Jupyter Lab gestartet hat. Das ist der Fall, wenn ein Text wie folgender im Terminal ausgegeben wird:
```
    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-6-open.html
    Or copy and paste one of these URLs:
        http://(dee70a5e518b or 127.0.0.1):8888/?token=112bb073331f1460b73768c76dffb2f87ac1d4ca7870d46a

```

Um auf Jupyter Lab aus einem lokal laufenden Browser zuzugreifen, haben Sie zwei Möglichkeiten:

* Ändern Sie in der URL den Host-Teil auf `localhost`. Im Beispiel oben würde sich `http://localhost:8888/?token=112bb073331f1460b73768c76dffb2f87ac1d4ca7870d46a` ergeben (bei Ihnen wird das Token ein anderes sein). 
  **oder**
* Gehen Sie auf http://localhost:8888/ und kopieren Sie das Token (im Beispiel oben `112bb073331f1460b73768c76dffb2f87ac1d4ca7870d46a`; bei Ihnen wird es ein anderes sein) in das entsprechende Formular-Feld.

#### Hinweise:

* Das aktuelle Host-Verzeichnis wird im Container (und in Jupyter Lab) als `work/` eingebunden. Sie können dieses Verzeichnis sowohl vom Host als auch von Jupyter Lab aus lesen und schreiben.  
  :::danger
  :warning: Alles im Container, was ausserhalb von `work/` liegt, geht **beim Beenden des Containers verloren!**
  :::

### Variante C: "Binder" im Web

(Nur als Not-Lösung, falls A und B nicht gehen. Ist wegen geteilter spendenfinanzierter Hardware-Ressourcen vermutlich deutlich langsamer.)

"Binder" (https://mybinder.org) ist eine Plattform, auf der vorbereitete Jupyter-Notebooks samt benötigter Software ausprobiert werden können. Dazu wird für jede Benutzersitzung ein Docker-Container auf der Plattform gestartet. [Dieser wird nach einer Weile automatisch wieder beendet und gelöscht.](https://mybinder.readthedocs.io/en/latest/faq.html#how-long-will-my-binder-session-last)

:::danger
:warning: Bei der automatischen Löschung des Containers geht alles verloren, was Sie nicht explizit auf Ihren eigenen Computer heruntergeladen haben.
:::

Um eine solche Sitzung zu starten, klicken Sie auf: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/smurve/HSR2019/master?urlpath=lab).



---

