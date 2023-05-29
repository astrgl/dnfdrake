%global gb3_ver %(gbc3 -V)

Name: dnfdrake
Version: 3.6.8
Release: 1
Packager: Astragalo
License: GPL
Group: Graphical desktop/KDE
Summary: DnfDrake  is a frontend for DNF
Url: https://mib.pianetalinux.org/
#Source: %{name}-%{version}.tar.gz
Source: https://github.com/astrgl/dnfdrake/archive/refs/tags/3.6.8.tar.gz

BuildRequires: gambas3-devel
BuildRequires: gambas3-gb-dbus
BuildRequires: gambas3-gb-form
BuildRequires: gambas3-gb-form-stock
BuildRequires: gambas3-gb-gtk3
BuildRequires: gambas3-gb-gui
BuildRequires: gambas3-gb-image
BuildRequires: gambas3-gb-qt5
BuildRequires: imagemagick

Requires: sudo
Requires: gambas3-runtime = %{gb3_ver}
Requires: gambas3-gb-form
Requires: gambas3-gb-image
Requires: gambas3-gb-gui
Requires: gambas3-gb-qt5
Requires: gambas3-gb-gtk3
Requires: gambas3-gb-dbus
Requires: gambas3-gb-form-stock
Requires: hicolor-icon-theme
Requires: dnf-utils
Requires: lsb-release
Requires: createrepo_c
Requires: python-dnf-plugin-versionlock
Requires: xrandr
Requires:dnfdraketray

BuildArch: noarch

#Conflicts:  gambas3-runtime  > 3.18.1

%description
DnfDrake  is a frontend for DNF package manager
Powerful like a terminal and simple like a GUI!

%prep
%autosetup -n %{name}-%{version}

%build
gbc3 -e -a -g -t  -f public-module -f public-control -j%{?_smp_mflags}
gba3
cp %{name}-%{version}.gambas %{name}.gambas

%install

install -Dm 755 dnfdrake.gambas -t %{buildroot}/%{_bindir}/
install -Dm 755 FILE-EXTRA/dnfdrake.desktop -t %buildroot/%_datadir/applications/
install -Dm 644 FILE-EXTRA/license -t %{buildroot}/%{_datadir}/dnfdrake/
install -Dm 644 FILE-EXTRA/dnfdrake-COMMAND -t %{buildroot}/%{_datadir}/dnfdrake/
install -Dm 644 FILE-EXTRA/dnfdrake-*-* -t %{buildroot}/%{_datadir}/dnfdrake/
install -Dm 644 dnfdrake.svg  -t %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/

%files
%{_bindir}/dnfdrake.gambas
%{_datadir}/applications/dnfdrake.desktop
%{_datadir}/icons/hicolor/32x32/apps/dnfdrake.svg
%{_datadir}/dnfdrake/license
%{_datadir}/dnfdrake/dnfdrake-COMMAND
%{_datadir}/dnfdrake/dnfdrake-*-*

%changelog
*Mon May 29 2023 Astragalo <mauro.carbini@gmail.com> 3.6.8-mib1
- Rebuild con nuovo sorgente
- Aggiunta conferma in uscita per alt+F4

*Wed May 03 2023 Astragalo <mauro.carbini@gmail.com> 3.6.7-mib1
- Rebuild con separazione dnfdraketray e nuovo sorgente

*Fri Apr 21 2023 Astragalo <mauro.carbini@gmail.com> 3.6.6-mib1
- Rebuild con Gambas 3.18.2 per OMA Cooker

*Sun Feb 26 2023 Astragalo <mauro.carbini@gmail.com> 3.6.5-mib1
- Rebuild con Gambas 3.18.1 per OMA Cooker

*Mon Feb 06 2023 Astragalo <mauro.carbini@gmail.com> 3.6.4-mib1
- Rebuild con Gambas 3.18.0 per OMA Cooker

*Sun Jan 15 2023 Astragalo <mauro.carbini@gmail.com> 3.6.3-mib1
- Correzione rilevazione distrosync sulla finestra extra

*Sun Jan 15 2023 Astragalo <mauro.carbini@gmail.com> 3.6.2-mib1
- Aggiunto Controllo distribuzione per OMA con cocker e ROMA usa distrosync di default

*Fri Dec 16 2022 Astragalo <mauro.carbini@gmail.com> 3.6.0-mib1
- Rilascio versione pubblica 3.6.0

*Thu Dec 15 2022 Astragalo <mauro.carbini@gmail.com> 3.5.21-mib1
- Aggiornamento di DnfDrakeTray versione 2.0.7 dovrebbe sistemare la posizione della finestra

*Thu Dec 15 2022 Astragalo <mauro.carbini@gmail.com> 3.5.20-mib1
- Corretto bug che su chiusura FPW con MYREPO aperto in securemode riattivava Fmain

*Wed Dec 14 2022 Astragalo <mauro.carbini@gmail.com> 3.5.19-mib1
- Corretto bug LINE Fmain.#hProcess.read.678 (' Wait 0.05  ' SE SI PREME ANNULLA SULLA FINESTRA DELLA PASSWORD IL PROGRAMMA VA IN STACKOVERFLOW)

*Tue Dec 13 2022 Astragalo <mauro.carbini@gmail.com> 3.5.18-mib1
- Corretto bug che abilita FMAIN a fine operazione anche con SECUREMODE attivo (inserita condizione in btnclose di FOK che non abilita se frun è visilile)
- Corretto bug che non attiva il securemode dopo aver lavorato con MYREPO (aggiunto Fmain.$FRUNPW = 1 sul ppulsante di chiusura)

*Mon Dec 12 2022 Astragalo <mauro.carbini@gmail.com> 3.5.17-mib1
- Prima versione per OMA per ricerca Bug

*Sun Dec 11 2022 Astragalo <mauro.carbini@gmail.com> 3.5.16-mib1
- Insertita traduzione e numero di versione finale 3.6.0

*Sun Dec 11 2022 Astragalo <mauro.carbini@gmail.com> 3.5.15-mib1
- Correzioni varie per autosuspend

*Sun Dec 11 2022 Astragalo <mauro.carbini@gmail.com> 3.5.12-mib1
- Intergrata la funzione Autosuspend sul pulsante di chiusura BTNCLOSE

*Sat Dec 10 2022 Astragalo <mauro.carbini@gmail.com> 3.5.11-mib1
- Aumentato il tempo per passaggio da FRESETSUSPEND e FRUN (wait 0.3)

*Sat Dec 10 2022 Astragalo <mauro.carbini@gmail.com> 3.5.10-mib1
- Fix della funzione AutoSuspend (dovrebbe essere funzionante, mancano traduzioni)

*Sat Dec 10 2022 Astragalo <mauro.carbini@gmail.com> 3.5.8-mib1
- Aggiunto $CLEARLOGSUSPEND = 1 in BTNNO FSINOSECURE

*Sat Dec 10 2022 Astragalo <mauro.carbini@gmail.com> 3.5.7-mib1
- Inserita  FRESETSUSPEND per il ripristino della sospensione dopo gli aggiornamenti

*Sat Dec 10 2022 Astragalo <mauro.carbini@gmail.com> 3.5.6-mib1
- Aggiunta la funzione AutoSuspend anche al pulsante di aggiornamento sistema btnupdate
- Create le funzioni DTSUPDATE e DSTSYNC i pulsanti ora richiamano quelle il codiceè stato spostato lì

*Fri Dec 09 2022 Astragalo <mauro.carbini@gmail.com> 3.5.5-mib1
- WATCHDOG disattivato
- Correzione di RECOVERSUSPEND

*Wed Dec 07 2022 Astragalo <mauro.carbini@gmail.com> 3.5.4-mib1
- Correzione WATCHDOG per FMAIN.ENABLE=FALSE non interviene se FMYREPO è aperto

*Wed Dec 07 2022 Astragalo <mauro.carbini@gmail.com> 3.5.3-mib1
- Correzione WATCHDOG per FMAIN.ENABLE=FALSE non interviene se FRUN è aperto

*Wed Dec 07 2022 Astragalo <mauro.carbini@gmail.com> 3.5.2-mib1
- Corretto il timing di DISTROSYNCWAIT portandoloda 1 sec a 0.2 sec

*Wed Dec 07 2022 Astragalo <mauro.carbini@gmail.com> 3.5.1-mib1
- Aggiunta funzione AutoSuspend che consente di disattivare e riabilitare il suspend durante gli aggiornamenti (per ora solo con distrosync)
- Piccoli fix in modalità non SECUREMODE
- WATCHGOD per FMAIN.ENABLE=FALSE dovrebbe evitare che la finestra principale rimanga disabilitata

*Tue Nov 15 2022 Astragalo <mauro.carbini@gmail.com> 3.5.0-mib1
- Modifica dnfdrake.desktop (messa maiuscola sul nome dnfdrake)
- Modifica pulsante Suspend
- Modifica immagini sui pulsanti, ora cliccandoci sopra esegue il click del pulsante

*Mon Nov 07 2022 Astragalo <mauro.carbini@gmail.com> 3.4.97-mib1
- Modifica posizione pulsanti

*Sun Nov 06 2022 Astragalo <mauro.carbini@gmail.com> 3.4.96-mib1
- Aggiunta tooltip a pulsante MyRepo

*Sat Nov 05 2022 Astragalo <mauro.carbini@gmail.com> 3.4.95-mib1
- Aggiunta tooltip a Suspend disable e riposizionate le icone

*Fri Nov 04 2022 Astragalo <mauro.carbini@gmail.com> 3.4.90-mib1
- Passaggio della versione Rosa a Gambas 3.17.3
- Aggiunta funzione Suspend disable (iniziale)

*Thu Oct 06 2022 Astragalo <mauro.carbini@gmail.com> 3.4.4-mib1
- Miglioramento del securemode in MYREPO(la finestra di password inibisce quella di MYREPO)

*Tue Sep 27 2022 Astragalo <mauro.carbini@gmail.com> 3.4.3-mib2
- Modifiche spec da Mandian OMA

*Thu Sep 22 2022 Astragalo <mauro.carbini@gmail.com> 3.4.3-mib1
- Fix bug nomi lughi su lista aggiornamenti

*Thu Sep 22 2022 Astragalo <mauro.carbini@gmail.com> 3.4.2-mib1
- Ora Myrepo all'apertura seleziona la prima voce della lista
- Pulizia codice Myrepo inserito CERCALSTREPO

*Thu Sep 22 2022 Astragalo <mauro.carbini@gmail.com> 3.4.1-mib1
- Versione2 di MyRepo con lista repo e stato

*Fri Sep 16 2022 Astragalo <mauro.carbini@gmail.com> 3.4.0-mib1
- Rilascio versione pubblica 3.4.0

*Thu Sep 15 2022 Astragalo <mauro.carbini@gmail.com> 3.3.100-mib1
- Aggiunta funzione securemode sul pulsante download

*Wed Sep 14 2022 Astragalo <mauro.carbini@gmail.com> 3.3.99-mib1
- Corretto bug che blocca avvio di dnfdrake se si utilizza la funzione reloadlang
- Corretto Bug risoluzione su comando reloadlang
- Corretto bug sul testo del pulsante command se si utilizza la funzione reloadlang

*Tue Sep 13 2022 Astragalo <mauro.carbini@gmail.com> 3.3.98-mib1
- Corretto bug che blocca avvio di dnfdrake se si avvia manualmente la tray
- Aggiunta gestione dimensione finestre FERROR e FSINOSECURE
- Cambiato testo pulsante disinstallazione da "Delete" in " Remove"

*Wed Sep 07 2022 Astragalo <mauro.carbini@gmail.com> 3.3.96-mib1
- Corretto Bug risoluzione su comando autoremove list
- Aggiunta tooltip a pulsanti risoluzione

*Tue Sep 06 2022 Astragalo <mauro.carbini@gmail.com> 3.3.95-mib1
- Aggiunto pulsante per ingrandire e rimpicciolire la finestra

*Mon Sep 05 2022 Astragalo <mauro.carbini@gmail.com> 3.3.90-mib1
- Aggiunta gestione dimensione finestra principale in base alla risoluzione dello schermo

*Wed Aug 31 2022 Astragalo <mauro.carbini@gmail.com> 3.3.3-mib1
- Correzione sulla finestra di Myrepo, ora il caricamento delle liste parte solo se ci sono modifiche
- Il tasto pulisci tutto lascia nel box il suffisso "MyRepo-"

*Tue Aug 30 2022 Astragalo <mauro.carbini@gmail.com> 3.3.2-mib1
- Correzione bug di Dnf list autoremove che con molti pacchetti crea la lista ma non rimuove, ora mosta i pulsanti di gestione

*Mon Aug 29 2022 Astragalo <mauro.carbini@gmail.com> 3.3.1-mib1
- Correzione colore di Dnf list autoremove da giallo ad arancio

*Sun Aug 28 2022 Astragalo <mauro.carbini@gmail.com> 3.3.0-mib1
- Verisone pubblica con funzione autoremove
- Correzione tootltip Dnf list autoremove

*Sat Aug 27 2022 Astragalo <mauro.carbini@gmail.com> 3.2.98-mib1
- Modificata funzione Dnf list autoremove ora di default seleziona tutti i pacchetti -versione test
- Aggiunta descrizione nel txtpkg durante Dnf list autoremove

*Fri Aug 26 2022 Astragalo <mauro.carbini@gmail.com> 3.2.95-mib1
- Aggiunta funzione Dnf list autoremove -versione test
- Altre correzioni sullo stato del mouse durante la ricerca

*Tue Aug 23 2022 Astragalo <mauro.carbini@gmail.com> 3.2.90-mib1
- Aggiunta funzione Dnf autoremove -versione test

*Tue Aug 16 2022 Astragalo <mauro.carbini@gmail.com> 3.2.0-mib1
- Aggiunto l'aggiornamento della cache di dnf se viene eseguito un rebuild dei repodata di un repo locale

*Sat Aug 13 2022 Astragalo <mauro.carbini@gmail.com> 3.2.0-mib1
- Rilascio versione 3.2.0
- Piccole correzioni sulle tootltip di MyRepo

*Wed Aug 10 2022 Astragalo <mauro.carbini@gmail.com> 3.1.96-mib1
- Aggiunte tootltip a Myrepo + altre correzioni
- rimossi dal sorgente i vecchi file di traduzione

*Tue Aug 09 2022 Astragalo <mauro.carbini@gmail.com> 3.1.95-mib1
- Aggiunta funzione MyRepo per la creazione dei repo personali

*Fri Jul 29 2022 Astragalo <mauro.carbini@gmail.com> 3.1.6-mib1
- Aggiunta la gestione del pulsante di lancio di OM-PICKER e visibile solo in OMA

*Sat Jul 02 2022 Astragalo <mauro.carbini@gmail.com> 3.1.5-mib1
- Ridimensionata la finestra in altezza (H700) per corretta visualizzazione in wayland

*Thu Jun 30 2022 Astragalo <mauro.carbini@gmail.com> 3.1.4-mib1
- Riscritta la visualizzazione dei paccheti in FSINOSECURE azzera i tempi di attesa
- Riscritta la visualizzazione di FERROR azzera i tempi di attesa

*Tue Jun 21 2022 Astragalo <mauro.carbini@gmail.com> 3.1.3-mib1
- Fix bug lingua di emergenza se lingua di sistema non supportata

*Thu Jun 09 2022 Astragalo <mauro.carbini@gmail.com> 3.1.2-mib1
- Aggiunta gestione securemode al pulsante OM-Picker
- Piccoli fix grafica

*Wed Jun 01 2022 Astragalo <mauro.carbini@gmail.com> 3.1.1-mib1
- Migliorata la gestione aggiornamento liste dopo esclusioni
- Aggiunta nuova funzionalità exclude

*Tue Apr 26 2022 Astragalo <mauro.carbini@gmail.com> 3.0.10-mib1
- fix bug su FERROR durante l'aggiornamento di un pacchetto

*Fri Apr 15 2022 Astragalo <mauro.carbini@gmail.com> 3.0.9-mib1
- Fix bug percorso  con spazi durante installazione, rimozione, ecc.
- Fix creazione fornato data e ora nel nome dei log

*Thu Apr 14 2022 Astragalo <mauro.carbini@gmail.com> 3.0.7-mib1
- Fix bug sul pulsante disinstalla

*Thu Mar 31 2022 Astragalo <mauro.carbini@gmail.com> 3.0.6-mib1
- Fix su tutti i pulsanti che chiudono finestre con "ME.Close" è stato aggiunto  "BTNnomeoulsante.Enable= False" per evitare errori sui doppi click
- Fix salvataggio comando $UPDATE distro non viene più sovrascritto col comando di "distro-sync"
- Fix BTNRETRY ora riprova in caso di distro sync o update senza cancellare la cache
- Fix BTNRETRY che genera un errore se viene dato un doppio click veloce

*Tue  Mar 29 2022 Astragalo <mauro.carbini@gmail.com> 3.0.4-mib1
- Fix su lingua catalana e altri minori

*Mon  Mar 28 2022 Astragalo <mauro.carbini@gmail.com> 3.0.3-mib1
- Aggiunto controllo che disabilita dnfdraketray se non è presente il supporto per la lingua di sistema

*Mon  Mar 28 2022 Astragalo <mauro.carbini@gmail.com> 3.0.2-mib1
- Aggiunto il supporto iniziale per la lingua Catalana

*Fri Mar 25 2022 Astragalo <mauro.carbini@gmail.com> 3.0.1-mib1
- Modifica nome file linguistici nel formato nomefile-xx_XX
- Modifica identificazione lingua in DnfDrake e DnfDrakeTray
- Aggiunta della funzionalita magiclang (consente di cambiare a caldo la lingua del programma digitando magiclang xx_XX in txtcommand)
- Aggiunta della funzionalita reloadlang (consente di caricare a caldo la lingua dell'nterfaccia del programma digitando reloadlang in txtcommand)

*Thu Mar 17 2022 Astragalo <mauro.carbini@gmail.com> 3.0.0-mib1
- Cambio numerazione per rilascio
- Fix tootltip Btnpathpkglist

*Tue Mar 15 2022 Astragalo <mauro.carbini@gmail.com> 2.99.1-mib1
- Fix pulsante download ora sesi annulla dalla finestra di dialogo non scarica più nulla 

*Tue Mar 15 2022 Astragalo <mauro.carbini@gmail.com> 2.99.0-mib1
- Cambio numerazione in prerilascio
- Fix  bug in $PATHDIR e $PATHLOG 
- Modificato il controllo che provvede a verificare se sono stati selezionati troppi pacchetti col pulsante Updatepkg (>5) e nel caso crea una lista temporanea e raccomanda l'uso del pulsante aggiorna sistema.

*Sat Mar 12 2022 Astragalo <mauro.carbini@gmail.com> 2.1.29-mib1
- Aggiunto un controllo che provvede a verificare se sono stati selezionati troppi pacchetti e nel caso crea una lista temporanea per evitare errori

*Sat Mar 12 2022 Astragalo <mauro.carbini@gmail.com> 2.1.28-mib1
- Modificata la gestione delle liste locali ora un pulsante serve per creare file di liste .txt e l'altro crea le liste in automatico se si tenta di installare molti pacchetti assieme
- Inseriti altri controlli per evitare blocchi se si chiudono  FINSTALL, FERROR, FERESUMEUPDATE,ECC  a causa dell'enable di FMAIN (forse Inseriti tutti)

*Fri Mar 11 2022 Astragalo <mauro.carbini@gmail.com> 2.1.27-mib1
- Ridimensionata la finestra di FSINOSECURE
- Fix Fmain abilitata  dopo riapertura di FPW per errore password
- Aggiunta funzione IGNORECASE sulla ricerca offline con opzione in extra e memoria dell'impostazione
- Fix setfocus sul pulsante si in FSINOSECURE

*Thu Mar 10 2022 Astragalo <mauro.carbini@gmail.com> 2.1.24-mib1
- Fix blocco apparente quando FSINOSECURE deve visualizzare molti pacchetti, ora li scrive uno per volta anzichè tutti alla fine
- Inseriti alcuni controlli per evitare blocchi se si chiudono finestre come FPW, FSINO, ecc a causa dell'enable di FMAIN

*Tue Mar 08 2022 Astragalo <mauro.carbini@gmail.com> 2.1.23-mib1
- Aggiunto tooltip su gestione liste temporanee
- Fix apertura FRUN per installazione/rimozione da lista pacchetti personalizzata

*Tue Mar 08 2022 Astragalo <mauro.carbini@gmail.com> 2.1.22-mib1
- Fix sulla pulizia delle liste temporanee eliminato il comando da BTNCLEAR
- Aggiunta la funzione per salvare le liste temporanee
- Sostituite le scritte con icone sui pulsante di gestione delle liste temporanee

*Mon Mar 07 2022 Astragalo <mauro.carbini@gmail.com> 2.1.21-mib1
- Riscritta tutta la gestione delle liste temporanee
- Fix tooltip hbox1 del pulsante comando ora si vede solo se il box è attivo

*Sun Mar 06 2022 Astragalo <mauro.carbini@gmail.com> 2.1.19-mib1
- Aggiunto ricaricamento delle liste dopo l'uso del pulsante dnf clean
- Aggiunto un messaggio che consiglia di usare i pulsanti di aggiornamento sistema se si tenta di aggiornare molti pacchetti

*Sun Mar 06 2022 Astragalo <mauro.carbini@gmail.com> 2.1.19-mib1
- Aggiunta tooltip a btnaddpkglist
- Piccoli fix

*Sat Mar 05 2022 Astragalo <mauro.carbini@gmail.com> 2.1.18-mib1
- Aggiornata l'icona del pulsante custom command
- Aggiunta un'icona al pulsante distro update 

*Sat Mar 05 2022 Astragalo <mauro.carbini@gmail.com> 2.1.17-mib1
- Aggiunta la gestione di liste temporanee per installazione/rimozione pacchetti consente di selezionare in più step

*Thu Mar 03 2022 Astragalo <mauro.carbini@gmail.com> 2.1.16-mib1
- Fix icone mancanti su finestre secondarie
- Aggiunta la funzione info tramite tasto destro su un pacchetto delle liste
- Aggiunte tootltip sulle liste dei pacchetti

*Tue Mar 01 2022 Astragalo <mauro.carbini@gmail.com> 2.1.15-mib1
- Aggiunta la funzionalità GuideButton che col securemode attivo abilita solo i pulsanti utilizzabili

*Tue Mar 01 2022 Astragalo <mauro.carbini@gmail.com> 2.1.12-mib1
- Aggiunta tooltip su Btnpathpkglist
- Modificato il pulsante sulla finestra di errore ora esegue "dnf clean package" e non "dnf clean cache"
- Altri piccoli fix

*Tue Mar 01 2022 Astragalo <mauro.carbini@gmail.com> 2.1.11-mib1
- Fix resumeupdate ora visualizza il pacchetti che va ad installare
- Fix resumeupdate ora riconosce se ci sono paccheti in/var/cache/dnf/... cambiata la stringa di controllo
- Ripristinato il buffer del $hProcess (2560) non dovrebbe essere necessario dopo l'introduzione delle liste di installazione

*Mon Feb 28 2022 Astragalo <mauro.carbini@gmail.com> 2.1.10-mib1
- Aggiunta la possibilità di installar, rimuovere ,aggiornare, ecc. i pacchetti riportati in una lista (nomefile.txt)
- Aggiunta la funzione per creare la lista dei pacchetti da installare selezionandoli in una cartella
- Sistemazione passaggio da log a nolog ora disattiva il securemode che senza log non funziona
- Sistemazione di modo verbose ora se attivato disattiva in automatico log e securemode
- Fix del bug sulla visualizzazionedi FPW e FRUN assieme (inserito un timer in FPW)
- Aumentato il buffer del $hProcess (5120)per accettare stringhe più lunghe durante l'installazione di più pacchetti in manuale


*Thu Feb 24 2022 Astragalo <mauro.carbini@gmail.com> 2.1.8-mib1
- Attivati tutti i pulsanti nell'interfaccia e disabilitati i controlli in extra
- Aggiunta traduzione al pulsante Retry nella gestione errori in securemode

*Tue Feb 22 2022 Astragalo <mauro.carbini@gmail.com> 2.1.7-mib1
- Securemode modalità di default
- Aggiunta la gestione errori in securemode  
- Corretto bug della chiusura di FPW col pulsante annulla dopo aver sbagliato la password

*Sun Feb 06 2022 Astragalo <mauro.carbini@gmail.com> 2.1.6-mib1
- Altri Fix su funziona securemode

*Mon Jan 31 2022 Astragalo <mauro.carbini@gmail.com> 2.1.5-mib1
- Fix su funziona securemode (integrata su finestra resumeupdate)

*Sun Jan 30 2022 Astragalo <mauro.carbini@gmail.com> 2.1.4-mib1
- Aggiunta la securemode attivabile in configurazione  di default resta la nosecuremode
- Le modifiche  della 2.1.0 sono state raggruppate nella modalità securemode 

*Wed Jan 26 2022 Astragalo <mauro.carbini@gmail.com> 2.1.3-mib1
- Fix e migliorie delle modifiche della 2.1.0
- Aggiunto pulsante extra dnf clean cache

*Mon Jan 24 2022 Astragalo <mauro.carbini@gmail.com> 2.1.2-mib1
- Fix e migliorie delle modifiche della 2.1.0
- Ripristinate le notifiche aggiuntive delle finestre di dialogo  (password, liste, SI/NO, ecc)


*Sun Jan 23 2022 Astragalo <mauro.carbini@gmail.com> 2.1.0-mib1
- Eliminate le notifiche aggiuntive delle finestre di dialogo  (password, liste, SI/NO, ecc)
- Aggiunta finestra di progress installazione/disinstallazione/aggiornamento/ecc.
- Fix bug pulsante log con liste di ricerca attive ora esegue la piluzia prima di aprire la finestra dei log
- Le finestre di dialogo (password, liste, SI/NO, ecc) disabilitano la finestra principale finchè non terminano
- Opzione di default registrazione del log

*Sun Jan 09 2022 Astragalo <mauro.carbini@gmail.com> 2.0.4-mib1
- Migliorata la routine di chiusura del programma

*Tue Dec  28 2021 Astragalo <mauro.carbini@gmail.com> 2.0.3-mi2
- Aggiunto supporto nella ricerca offline ed online  per znver1 e aarch64 
- Fix mouse occupato durante la ricerca

*Fri Dec  24 2021 Astragalo <mauro.carbini@gmail.com> 2.0.2-mib2
- Cambio versione di sviluppo in Gambas 3.16.3 per OMA
- Rebuild di dnfdrake.gambas e dnfdraketray.gambas

*Thu Dec  23 2021 Astragalo <mauro.carbini@gmail.com> 2.0.1-mib2
- Test per cocker 
- Fix bug bordi 
- Fix bug extra indicazione config default

*Sat  Dec  18 2021 Astragalo <mauro.carbini@gmail.com> 2.0.1-mib1
- Aggiunto bordo colorato durante la ricerca

*Thu Nov 18 2021 Astragalo <mauro.carbini@gmail.com> 2.0.0-mib1
- Cambio numerazione versione 2.0.0
- Fix mancata visualizzazione del log se è visualizzata una lista

*Tue Nov 16 2021 Astragalo <mauro.carbini@gmail.com> 1.99.1-mib1
- Preversione 2.0
- Spostata l'opzione verbose in extra
- Altro Fix del comando resume
- Impostato logattivo di default
- Fix funzionalità di CHKBTNDISTROUPDATE in extra
- Aggiunta funzione "replay" mostra log ultima operazione
- Spostata la finestra di DnfDrakeTray 2.0.3

*Mon Nov 01 2021 Astragalo <mauro.carbini@gmail.com> 1.20.10-mib2
- Rimossa la dipendenza di Dolphin

*Mon Nov 01 2021 Astragalo <mauro.carbini@gmail.com> 1.20.10-mib1
- Fix del comando resume

*Mon Nov 01 2021 Astragalo <mauro.carbini@gmail.com> 1.20.9-mib1
- Fix del comando nel passaggio tra distro-sync e distro-update
- inserimento funzione resume su distro-update
- Riscritta la fuzione DATATIME per riformattare la data per il nome logfile

*Sun Oct 31 2021 Astragalo <mauro.carbini@gmail.com> 1.20.7-mib2
- Fix su interfaccia

*Sun Oct 31 2021 Astragalo <mauro.carbini@gmail.com> 1.20.7-mib1
- Aggiunta l'indicazione di data e ora sul file di log
- Aggiunta la funzione DATATIME che crea una stringa con data e ora
- Aggiunta la gestione dell'indicatore del mouse occupato durante le attività di installazione, aggiornamento, ecc
- Implementata la gestione interna dei log con apertura nel monitor di dnfdrake

*Tue Oct 26 2021 Astragalo <mauro.carbini@gmail.com> 1.20.5-mib1
- Aggiunta la gestione delle parola chiave "Non riuscito" in tutte le leingue tranne brasiliano
- Inviato su /dev/null output console quando non richiesto il log
- Fix su funzione verbose mode

*Sun Oct 24 2021 Astragalo <mauro.carbini@gmail.com> 1.20.2-mib1
- Aggiunto pulsante per apertura dolphin sulla cartella dei log
- Aggiunta l'opzione verbose mode
- Aggiunta la funzione log su aggiornamento e sincronizzazione distro

*Sun Oct 10 2021 Astragalo <mauro.carbini@gmail.com> 1.19.10-mib1
- Fix funzione resume su distro-sync
- Inserito in DnfDrake il modulo per evitare avvii multipli
- In DnfDrakeTray 2.0.2 corretta la gestione delle istanze multiple basata su intero anziche su stringa
- In DnfDrakeTray 2.0.1 corretta la gestione delle istanze multiple ora funziona
- In DnfDrakeTray 2.0.0 riscritta l'identificazione della lingua e la gestione delle istanze multiple

*Wed Sep 29 2021 Astragalo <mauro.carbini@gmail.com> 1.19.8-mib1
- Aggiunto supporto per la traduzione nella finestra Finstall

*Sat Sep 18 2021 Astragalo <mauro.carbini@gmail.com> 1.19.7-mib2
- Aggiunta funzione resume su distro-sync

*Tue Sep 7 2021 Astragalo <mauro.carbini@gmail.com> 1.19.6-mib1
- Aggiunta funzione reinstalla pacchetto (attivare in extra)

*Sun Sep 5 2021 Astragalo <mauro.carbini@gmail.com> 1.19.5-mib1
- Fix $MEMOCOMMAND dopo il cambio di pront

*Fri Sep 3 2021 Astragalo <mauro.carbini@gmail.com> 1.19.4-mib1
-Aggiunto il pulsante aggiorna alla finestra FINSTALL

*Thu Sep 2 2021 Astragalo <mauro.carbini@gmail.com> 1.19.3-mib3
- 3° step per l'installazione rpm con doppio click
- Modificato file dnfdrake.desktop inserito mimetype

*Tue Aug 31 2021 Astragalo <mauro.carbini@gmail.com> 1.19.2-mib1
- Riscritta la rilevazione della lingua di sistema
- 2° step per l'installazione rpm con doppio click

*Sun Aug 22 2021 Astragalo <mauro.carbini@gmail.com> 1.19.1-mib1
- Inizio supporto assistenza all'installazione rpm con doppio click

*Sun Aug 22 2021 Astragalo <mauro.carbini@gmail.com> 1.19.0-mib1
- Aggiunto skip a loadlist

*Tue Aug 17 2021 Astragalo <mauro.carbini@gmail.com> 1.18.8-mib3
- Aggiunta la traduzione per il nuovo pront sh (nel file TTP)

*Mon  Aug 16 2021 Astragalo <mauro.carbini@gmail.com> 1.18.7-mib1
- Modifica pront sh
- Aggiunto un comando di pulizia se si seleziona annulla finestra password

*Mon  Aug 16 2021 Astragalo <mauro.carbini@gmail.com> 1.18.6-mib1
- Nascosto pulsante OMPICKER
- Sostituito bash con sh nel processo ($hProcess line 78)
- Aggiunto un comando di pulizia se si seleziona NO

*Sun  Aug 15 2021 Astragalo <mauro.carbini@gmail.com> 1.18.5-mib1
- Primo build per Rosa R12

*Fri  Jul 09 2021 Astragalo <mauro.carbini@gmail.com> 1.18.4-mib1
-Fix minori  traduzioni e tooltip

*Sun  Jun 27 2021 Astragalo <mauro.carbini@gmail.com> 1.18.2-mib2
- Aggiunto supporto per la lingua tedesca (solo KEY)

*Sun  Jun 27 2021 Astragalo <mauro.carbini@gmail.com> 1.18.2-mib1
- Aggiunto supporto per la lingua spagnolo (solo KEY)

*Sat  Jun 26 2021 Astragalo <mauro.carbini@gmail.com> 1.18.1-mib2
- Aggiunto supporto per la lingua brasiliana (solo KEY)

*Thu Jun 24 2021 Astragalo <mauro.carbini@gmail.com> 1.18.0-mib1
- Aggiunta gestione recovery mode per mancanza supporto lingua

*Sat  Jun 12 2021 Astragalo <mauro.carbini@gmail.com> 1.17.35-mib2
- Sostituito su info la voce changelog con provides
- Aggiunto pulsante per visualizzare la password digitata 

*Tue Jun 08 2021 Astragalo <mauro.carbini@gmail.com> 1.17.34-mib1
- Aggiunta lingua inglese GB

*Sun Jun 06 2021 Astragalo <mauro.carbini@gmail.com> 1.17.33-mib2
-Test icona

*Wed Jun 2 2021 Astragalo <mauro.carbini@gmail.com> 1.17.32-mib3
- Migliorata la gestione del tasto pulisci quando le liste sono attive altrimenti non installa i pacchetti da txtpkg
- Test nuova icona

*Wed Jun 2 2021 Astragalo <mauro.carbini@gmail.com> 1.17.31-mib2
- Test icona

*Mon May 31 2021 Astragalo <mauro.carbini@gmail.com> 1.17.31-mib1
- Riposizionati pulsanti di Versionlock

*Sun May 30 2021 Astragalo <mauro.carbini@gmail.com> 1.17.30-mib1
- Migliorata la gestione aggiorna distro (Rolling/Cooker)

*Sun May 23 2021 Astragalo <mauro.carbini@gmail.com> 1.17.29-mib1
- Fix a funzione aggiorna distro (Rolling/Cooker)

*Fri May 21 2021 Astragalo <mauro.carbini@gmail.com> 1.17.28-mib1
- Fix a funzione aggiorna distro (Rolling/Cooker)

*Fri May 21 2021 Astragalo <mauro.carbini@gmail.com> 1.17.27-mib1
- Modifiche a funzione aggiorna distro (Rolling/Cooker)

*Wed May  19 2021 Astragalo   <mauro.carbini@gmail.com> 1.17.26-mib2
- Aggiunta iniziale funzione aggiorna distro

*Wed May  19 2021 Astragalo   <mauro.carbini@gmail.com> 1.17.26-mib1
- Aggiunta iniziale funzione aggiorna distro

*Tue May    18 2021 Astragalo   <mauro.carbini@gmail.com> 1.17.25-mib1
- Inserita finestra per inserimento selezione a domande di dnf
- Modificato gestione txtpkg ora basta digitare il nome e dare invio per cercare

*Sun May    16 2021 Astragalo   <mauro.carbini@gmail.com> 1.17.24-mib1
-Migliorata  la gestione se indowngrade non viene selezionato un pacchetto

*Sun May    16 2021 Astragalo   <mauro.carbini@gmail.com> 1.17.23-mib1
-Migliorata  la gestione se in installa,rimozione,aggiornamento non viene selezionato un pacchetto

*Sun May    16 2021 Astragalo   <mauro.carbini@gmail.com> 1.17.22-mib1
-Completato funzione versionlock

*Tue May    11 2021 Astragalo   <mauro.carbini@gmail.com> 1.17.21-mib1
-Aggiunta funzione iniziale versionlock

*Fri May    07 2021 Astragalo   <mauro.carbini@gmail.com> 1.17.20-mib1
-Fix minori

*Fri May    07 2021 Astragalo   <mauro.carbini@gmail.com> 1.17.19-mib15
- Aggiunto conflitto con Gambas maggiore 3.15.2-6

*Sun  May 02 2021 Astragalo <mauro.carbini@gmail.com> 1.17.19-mib1
- Aggiunta notifica se non trova pacchetti nella ricerca offline

*Sun  May 02 2021 Astragalo <mauro.carbini@gmail.com> 1.17.18-mib2
- Aggiunta selezione multipla rpm locali da installare

*Sun  May 02 2021 Astragalo <mauro.carbini@gmail.com> 1.17.18-mib1
- Aggiunta selezione multipla rpm locali da installare

*Sat  May 01 2021 Astragalo <mauro.carbini@gmail.com> 1.17.17-mib1
- Fix minori

*Sat  May 01 2021 Astragalo <mauro.carbini@gmail.com> 1.17.16-mib1
- Aggiunta nuova gestione  colorazione alle liste sulla ricerca offline tramite finestra config

*Tue Apr  27 2021 Astragalo <mauro.carbini@gmail.com> 1.17.15-mib1
- Fix minori

*Fri  Apr  23 2021 Astragalo <mauro.carbini@gmail.com> 1.17.12-mib1
- Aggiunta nuova colorazione alle liste sulla ricerca offline 

*Thu  Apr  22 2021 Astragalo <mauro.carbini@gmail.com> 1.17.11-mib1
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


