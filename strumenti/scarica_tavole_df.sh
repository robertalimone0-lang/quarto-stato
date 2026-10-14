#!/bin/sh
# Scarica dal Dipartimento delle Finanze le tavole IRPEF usate in dati/spese_fiscali (dichiarazioni 2025, anno d'imposta 2024).
# Codici: ...03 = ventili di reddito complessivo, ...02 = classi di reddito complessivo.
set -e
B="https://www1.finanze.gov.it/finanze/analisi_stat/public/index.php"
cd "$(dirname "$0")/../dati/spese_fiscali/tavole"
for c in 2025AAPFTOT020803 2025AAPFTOT020903 2025AAPFTOT021003 2025AAPFTOT020703 2025AAPFTOT020403; do
  curl -sL --http1.1 "$B?tree=$c&page=1&media=media&personalizza=no&export=3" -o "v_$c.csv"
done
curl -sL --http1.1 "$B?tree=2025AAPFTOT020802&page=1&media=media&personalizza=no&export=3" -o "c_2025AAPFTOT020802.csv"
