%define name dnfdrake
%define version 1.17.12
%define release %mkrel 2

Name: %{name}
Version: %{version}
Release: %{release}
Packager: Astragalo
License: GPL
Group: Graphical desktop/KDE
Summary: DnfDrake  is a frontend for DNF. Powerful like a terminal and simple like a GUI!
Url: http://www.
Source: dnfdrake_1.17.12.tar.gz
Requires:	sudo
Requires: gambas3-runtime
Requires: gambas3-gb-form
Requires: gambas3-gb-image
Requires: gambas3-gb-gui
Requires: gambas3-gb-qt5
Requires: gambas3-gb-gtk3
Requires: gambas3-gb-dbus
Requires: hicolor-icon-theme
Requires: dnf-utils
BuildArch:	noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
DnfDrake  is a frontend for DNF package manager.

%prep
%setup -n dnfdrake

%install
rm -rf %{buildroot}

mkdir %buildroot
mkdir %buildroot/usr
mkdir %buildroot/%_bindir
mkdir %buildroot/%_datadir
mkdir %buildroot/%_datadir/applications
mkdir %buildroot/%_datadir/icons
mkdir %buildroot/%_datadir/icons/hicolor
mkdir %buildroot/%_datadir/icons/hicolor/32x32
mkdir %buildroot/%_datadir/icons/hicolor/32x32/apps
mkdir %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake.gambas %buildroot/%_bindir/
install -Dm 755 dnfdraketray.gambas %buildroot/%_bindir/
install -Dm 755 dnfdrake.desktop %buildroot/%_datadir/applications
install -Dm 755 license %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-COMMAND %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-BTN-IT %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-BTN-US %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-BTN-FR %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-BTN-PL %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-KEY-IT %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-KEY-US %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-KEY-FR %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-KEY-PL %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-TTP-IT %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-TTP-US %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-TTP-FR %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-TTP-PL %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-CMBI-IT %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-CMBI-US %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-CMBI-FR %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-CMBI-PL %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-CMBT-IT %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-CMBT-US %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-CMBT-FR %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-CMBT-PL %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-ABOUT-IT %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-ABOUT-US %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-ABOUT-FR %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake-ABOUT-PL %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdraketray.gambas.desktop %buildroot/%_datadir/dnfdrake
install -Dm 755 dnfdrake.svg  %buildroot/%_datadir/icons/hicolor/32x32/apps

%clean
rm -rf %{buildroot}

%files
%_bindir/dnfdrake.gambas
%_bindir/dnfdraketray.gambas
%_datadir/applications/dnfdrake.desktop
%{_datadir}/icons/hicolor/32x32/apps/dnfdrake.svg
%_datadir/dnfdrake/license
%_datadir/dnfdrake/dnfdrake-COMMAND
%_datadir/dnfdrake/dnfdrake-BTN-IT
%_datadir/dnfdrake/dnfdrake-BTN-US
%_datadir/dnfdrake/dnfdrake-BTN-FR
%_datadir/dnfdrake/dnfdrake-BTN-PL
%_datadir/dnfdrake/dnfdrake-KEY-IT
%_datadir/dnfdrake/dnfdrake-KEY-US
%_datadir/dnfdrake/dnfdrake-KEY-FR
%_datadir/dnfdrake/dnfdrake-KEY-PL
%_datadir/dnfdrake/dnfdrake-TTP-IT
%_datadir/dnfdrake/dnfdrake-TTP-US
%_datadir/dnfdrake/dnfdrake-TTP-FR
%_datadir/dnfdrake/dnfdrake-TTP-PL
%_datadir/dnfdrake/dnfdrake-CMBI-IT
%_datadir/dnfdrake/dnfdrake-CMBI-US
%_datadir/dnfdrake/dnfdrake-CMBI-FR
%_datadir/dnfdrake/dnfdrake-CMBI-PL
%_datadir/dnfdrake/dnfdrake-CMBT-IT
%_datadir/dnfdrake/dnfdrake-CMBT-US
%_datadir/dnfdrake/dnfdrake-CMBT-FR
%_datadir/dnfdrake/dnfdrake-CMBT-PL
%_datadir/dnfdrake/dnfdrake-ABOUT-IT
%_datadir/dnfdrake/dnfdrake-ABOUT-US
%_datadir/dnfdrake/dnfdrake-ABOUT-FR
%_datadir/dnfdrake/dnfdrake-ABOUT-PL
%_datadir/dnfdrake/dnfdraketray.gambas.desktop

%changelog
*Fri  Apr  23 2021 Astragalo <mauro.carbini@gmail.com> 1.17.12-mib1
- Aggiunta nuova colorazione alle liste sulla ricerca offline 

*Tue  Apr  22 2021 Astragalo <mauro.carbini@gmail.com> 1.17.11-mib1
-Fix errore del file locktray dopo gestione lista aggiornamenti

*Wed Apr 21 2021 Astragalo <mauro.carbini@gmail.com> 1.17.10-mib1
- Aggiunta funzionalità per pulsante download per ricordare il path all'interno della sessione
- Nuova funzionalità in caso di aggiornamenti disponibili DnfDrake carica la lista dei pacchetti aggiornamentidisponibili
-Dnfdraketray imposta un carattere a 0 se non ci sono aggiornamenti a 1 se disponibili

*Mon Apr 19 2021 Astragalo <mauro.carbini@gmail.com> 1.17.9-mib1
- Integrata nuova gestione per pulsante download
- Migliorata visibilita testo about
- Attivata funzione mouse occupato su ricerca pacchetto

*Sun Apr 18 2021 Astragalo <mauro.carbini@gmail.com> 1.17.8-mib1
- Aggiornamento parziale traduzioni

*Sat Apr 17 2021 Astragalo <mauro.carbini@gmail.com> 1.17.7-mib2
- Altri miglioramenti  gestione dei pulsanti installa rimuovi ecc.

*Sat Apr 17 2021 Astragalo <mauro.carbini@gmail.com> 1.17.7-mib1
- Altri miglioramenti  gestione dei pulsanti installa rimuovi ecc.

*Sat Apr 17 2021 Astragalo <mauro.carbini@gmail.com> 1.17.6-mib1
- Altri miglioramenti  gestione dei pulsanti installa rimuovi ecc.

*Sat Apr 17 2021 Astragalo <mauro.carbini@gmail.com> 1.17.5-mib1
- Migliorata gestione dei pulsanti installa rimuovi ecc.

*Sat Apr 17 2021 Astragalo <mauro.carbini@gmail.com> 1.17.4-mib1
- Pulsante aggiorna pacchetti sempre visibile più altre modifiche minori

*Sat Apr 17 2021 Astragalo <mauro.carbini@gmail.com> 1.17.3-mib1
- Modifiche in tutti i settori base per versione (ricerca, installazione, gestione offline, ecc) 2.0! 
*Wed Apr 14 2021 Astragalo <mauro.carbini@gmail.com> 1.17.0-mib1
- Inizio implementazione nuovo sistema di ricerca offline 

*Sat Apr 10 2021 Astragalo <mauro.carbini@gmail.com> 1.16.2-mib1
- Implementata selezione con doppioclicksu liste aggiuntive a tab con selezione tutti  

*Sat Apr 10 2021 Astragalo <mauro.carbini@gmail.com> 1.16.1-mib1
- Implementata selezione con doppioclicksu liste aggiuntive a tab con selezione tutti  

*Fri Apr 9 2021 Astragalo <mauro.carbini@gmail.com> 1.16.0-mib1
- Implementata nuova ricerca pacchetti a tab con selezione tutti  

*Tue  Apr  6 2021 Astragalo <mauro.carbini@gmail.com> 1.15.4-mib1
-Fix minori

*Tue  Apr  6 2021 Astragalo <mauro.carbini@gmail.com> 1.15.3-mib1
-Fix sfondo finestra di configurazione

*Tue  Apr  6 2021 Astragalo <mauro.carbini@gmail.com> 1.15.2-mib1
-Fix errore doppioclick in listpkg

*Mon  Apr 5 2021 Astragalo <mauro.carbini@gmail.com> 1.15.1-mib1
-Fix  avvio automatico di   dnfdraketray quando non esiste la cartella autostart in .config 

*Mon  Apr 5 2021 Astragalo <mauro.carbini@gmail.com> 1.15.0-mib1
-Aggiunto pulsante reset su extra dnfdraketray
-Fix  su  dnfdraketray

*Mon  Apr 5 2021 Astragalo <mauro.carbini@gmail.com> 1.12.12-mib2
-SHIFT+MOUSECLICK chiude dnfdraketray

*Mon  Apr 5 2021 Astragalo <mauro.carbini@gmail.com> 1.12.12-mib1
-Fix vari su  dnfdraketray

*Mon  Apr 5 2021 Astragalo <mauro.carbini@gmail.com> 1.12.11-mib2
-Cambiata l'icona di chiusura  dnfdraketray

*Mon  Apr 5 2021 Astragalo <mauro.carbini@gmail.com> 1.12.11-mib1
-Semplificazione funzioni  dnfdraketray

*Sun  Apr 4 2021 Astragalo <mauro.carbini@gmail.com> 1.12.10-mib3
-Fix vari su  dnfdraketray

*Sun  Apr 4 2021 Astragalo <mauro.carbini@gmail.com> 1.12.10-mib2
-Aggiunto D-bus component

*Sun  Apr 4 2021 Astragalo <mauro.carbini@gmail.com> 1.12.10-mib1
-Fix vari su  dnfdraketray

*Sun  Apr 4 2021 Astragalo <mauro.carbini@gmail.com> 1.12.9-mib1
-Abortita

*Sat  Apr  3 2021 Astragalo <mauro.carbini@gmail.com> 1.12.8-mib1
-Fix opzione che  all'avvio  dnfdraketray

*Sat  Apr  3 2021 Astragalo <mauro.carbini@gmail.com> 1.12.7-mib1
-Inserita opzione lancia all'avvio  dnfdraketray

*Sat  Apr  3 2021 Astragalo <mauro.carbini@gmail.com> 1.12.6-mib1
-Rimosso il menu contestuale da dnfdraketray

*Fri  Apr  2 2021 Astragalo <mauro.carbini@gmail.com> 1.12.5-mib1
-Ridisegnato il popoup
-Modifica testo pulsante in extra da chiudi ad applica

*Thu  Apr  1 2021 Astragalo <mauro.carbini@gmail.com> 1.12.4-mib1
-Aggiunto supporto per altre lingue e chiusura automatica popup

*Thu  Apr  1 2021 Astragalo <mauro.carbini@gmail.com> 1.12.3-mib1
-Migliorata la gestione di  dnfdraketray in dnfdrake >extra

*Thu  Apr  1 2021 Astragalo <mauro.carbini@gmail.com> 1.12.2-mib1
-Evita l'apertura di più istanze di dnfdraketray

*Thu  Apr  1 2021 Astragalo <mauro.carbini@gmail.com> 1.12.1-mib1
-Inizio funzionanalità trayicon

*Wed  Mar  31 2021 Astragalo <mauro.carbini@gmail.com> 1.12.0-mib1
-Modifiche alla finestra extra
-Inizio funzionanalità trayicon

*Sat  Mar  27 2021 Astragalo <mauro.carbini@gmail.com> 1.11.1-mib1
-Aggiunta la funzionalità extra options

*Sat  Mar  27 2021 Astragalo <mauro.carbini@gmail.com> 1.11.0-mib2
-Aggiunta la funzionalità extra options

*Sat  Mar  27 2021 Astragalo <mauro.carbini@gmail.com> 1.10.1-mib2
-Fix tooltip

*Sat  Mar  27 2021 Astragalo <mauro.carbini@gmail.com> 1.10.1-mib1
-Fix tooltip

*Sat  Mar  27 2021 Astragalo <mauro.carbini@gmail.com> 1.10.0-mib1
-Aggiunti pulsanti per downgrade e comando customi 

*Sat  Mar  27 2021 Astragalo <mauro.carbini@gmail.com> 1.9.6-mib1
-Altri Fix  analisi stream e ricerca nomi 

*Fri  Mar  26 2021 Astragalo <mauro.carbini@gmail.com> 1.9.5-mib2
-rebuild

*Fri  Mar  26 2021 Astragalo <mauro.carbini@gmail.com> 1.9.5-mib1
-Altri Fix  di ricerca in listpkg 

*Fri  Mar  26 2021 Astragalo <mauro.carbini@gmail.com> 1.9.4-mib1
-Fix e Miglioramneto dei criteri di ricerca in listpkg 

*Wed  Mar  24 2021 Astragalo <mauro.carbini@gmail.com> 1.9.3-mib1
-Fix bug con listpkg e tastoo info

*Tue  Mar  23 2021 Astragalo <mauro.carbini@gmail.com> 1.9.2-mib1
-Fix errore all'avvio dovuto ad aggiornamento da 1.8.x
-Modifica identificazione lingua per funzionare anche con le live

*Mon  Mar  22 2021 Astragalo <mauro.carbini@gmail.com> 1.9.0-mib1
-Possibilità di aggiornare i pacchetti selzionandoli nella ListPKG
-Miglioramneto della funzione trova aggiornamenti

*Sun  Mar  21 2021 Astragalo <mauro.carbini@gmail.com> 1.8.0-mib1
-Riscritto selezione e pulizia della listpkg (suggerimento Gianluigi di Gambas.it)
-Fix supporto per la lingua polacco (Andry Penguin)

*Sun  Mar  21 2021 Astragalo <mauro.carbini@gmail.com> 1.7.1-mib1
-Aggiunto supporto iniziale per la lingua polacco (Andry Penguin)

*Sat  Mar  20 2021 Astragalo <mauro.carbini@gmail.com> 1.7.0-mib1
-Aggiunta la possibilità di configurare i comandi Update install e Uninstall 
-Fix Bug minori

*Fri  Mar  19 2021 Astragalo <mauro.carbini@gmail.com> 1.6.1-mib1
-Gestione degli spazi prima e dopo il nome del pacchetto 

*Fri  Mar  19 2021 Astragalo <mauro.carbini@gmail.com> 1.6.0-mib1
-Aggiunto il supporto alla ricera dell'elenco dei file di un pacchetto

*Fri  Mar  19 2021 Astragalo <mauro.carbini@gmail.com> 1.5.6-mib1
-Altri Fix sulla ricerca listpkg
-Completata la traduzione in francese (Raphael)

*Thu  Mar  18 2021 Astragalo <mauro.carbini@gmail.com> 1.5.5-mib1
-Altri Fix sulla ricerca listpkg

*Thu  Mar  18 2021 Astragalo <mauro.carbini@gmail.com> 1.5.4-mib1
-Fix crash sul doppio click della Lispkg quando viene eseguito nasconde il pulsante scrivi che altrimenti genera crash

*Thu  Mar  18 2021 Astragalo <mauro.carbini@gmail.com> 1.5.4-mib1
-Fix crash sulla pulizia della Lispkg quando è stato inviato un nome alla TXTPKG
-Aggiunta Requires: dnf-utils per ricerca file non installati

*Wed  Mar  17 2021 Astragalo <mauro.carbini@gmail.com> 1.5.3-mib1
-Fix al supporto lingua francese

*Tue  Mar  16 2021 Astragalo <mauro.carbini@gmail.com> 1.5.2-mib1
-Supporto alla ricerca file nei pacchetti installati

*Tue  Mar  16 2021 Astragalo <mauro.carbini@gmail.com> 1.5.1-mib1
-Soppressa

*Tue  Mar  16 2021 Astragalo <mauro.carbini@gmail.com> 1.5.0-mib1
-Supporto iniziale per il francese

*Sun  Mar  14 2021 Astragalo <mauro.carbini@gmail.com> 1.4.0-mib1
-Aggiunto pulsante lancio OM-Repo-Picker

*Sat  Mar  13 2021 Astragalo <mauro.carbini@gmail.com> 1.3.5-mib1
-Aggiornamento traduzioni (Rugyada)
-Il doppioclick su txtpkg calcella txtpkg prima di inviare il pacchetto


*Sat  Mar  13 2021 Astragalo <mauro.carbini@gmail.com> 1.3.4-mib1
-Fix path pulsante download 
-inserimento messaggio selezionare pacchetto
-inserimento About

*Fri  Mar  12 2021 Astragalo <mauro.carbini@gmail.com> 1.3.3-mib1
-Aggiunto pulsante cancella txtpkg e testo a sisnistra

*Thu Mar  11 2021 Astragalo <mauro.carbini@gmail.com> 1.3.2-mib1
-Aggiunto pulsante cancella txtpkg e testo a sisnistra

*Thu Mar  11 2021 Astragalo <mauro.carbini@gmail.com> 1.3.1-mib1
-Bugfix supporto linguistico alle combbox

*Thu Mar  11 2021 Astragalo <mauro.carbini@gmail.com> 1.3.0-mib1
-Esteso  supporto linguistico alle combbox
-Rimozione textbox di stato
-piccole modifiche layout

*Thu Mar  11 2021 Astragalo <mauro.carbini@gmail.com> 1.2.3-mib1
-Altro fix path supporto linguistico

*Wed Mar  10 2021 Astragalo <mauro.carbini@gmail.com> 1.2.2-mib1
-Fix path supporto linguistico

*Wed Mar  10 2021 Astragalo <mauro.carbini@gmail.com> 1.2.1-mib1
-Bug fix supporto linguistico
-Correzione altri  bug

*Mon Mar  08 2021 Astragalo <mauro.carbini@gmail.com> 1.2.0-mib1
-Aggiunto supporto per la lingua inglese
-Correzione altri  bug

*Sun Mar  07 2021 Astragalo <mauro.carbini@gmail.com> 1.1.0-mib1
-Inizio supporto linguistico
-Nuova icona (Rugyada)
-Correzione altri  bug

*Fri  Mar 05 2021 Astragalo <mauro.carbini@gmail.com> 1.0.1-mib1
-Correzione visualizzazione darkmode normalmode
-Correzione altri  bug

*Wed Mar 03 2021 Astragalo <mauro.carbini@gmail.com> 1.0-mib1
-Build for OpenMandriva 4.2 (MIB)


