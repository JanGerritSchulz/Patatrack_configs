#!/bin/bash

CONFIGNAME="$1"
shift

CUSTOMIZE=""
PROCMODIFIERS=""

mode=""
while [[ $# -gt 0 ]]; do
    case "$1" in
        --procMods) mode="procModifiers" ;;
        --custom) mode="customizations" ;;
        *)
            if [[ "$mode" == "customizations" ]]; then
                while IFS= read -r line || [[ -n "$line" ]]; do
                    if [[ ! "$line" =~ ^#.*  ]]; then
                        CUSTOMIZE+="$line;"
                    fi
                done < customizations/$1.py
            elif [[ "$mode" == "procModifiers" ]]; then
                PROCMODIFIERS="${PROCMODIFIERS}$1,"
            fi ;;
    esac
    shift
done

PROCMODIFIERS=${PROCMODIFIERS%,}
# CUSTOMIZE=${CUSTOMIZE%;}


# create the config file without procModifiers
if [ ! "$PROCMODIFIERS" ];then
    #,HLT:75e33_trackingOnly,VALIDATION:@hltValidation
    cmsDriver.py step_2 -s L1P2GT \
         --mc \
         --conditions auto:phase2_realistic_T33 \
         --datatier DQMIO \
         -n -1 \
         --eventcontent DQMIO \
         --geometry ExtendedRun4D110 \
         --era Phase2C17I13M9 \
         --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000 \
         --filein "REPLACEDINPUTFILES" \
         --fileout "Tracking_DQMIO.root" \
         --python_filename "temp_cfg.py" \
         --process SIMPIXELTRACKS \
         --inputCommands='keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT' \
         --customise_commands="$CUSTOMIZE" \
         --no_exec
else
    #,HLT:75e33_trackingOnly,VALIDATION:@hltValidation
    cmsDriver.py step_2 -s L1P2GT \
         --mc \
         --conditions auto:phase2_realistic_T33 \
         --datatier DQMIO \
         -n -1 \
         --eventcontent DQMIO \
         --geometry ExtendedRun4D110 \
         --era Phase2C17I13M9 \
         --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000 \
         --filein "REPLACEDINPUTFILES" \
         --fileout "Tracking_DQMIO.root" \
         --python_filename "temp_cfg.py" \
         --process SIMPIXELTRACKS \
         --inputCommands='keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT' \
         --customise_commands="$CUSTOMIZE" \
         --no_exec \
         --procModifiers $PROCMODIFIERS
fi

# modify the config to allow easy command line options when running cmsRun
python3 scripts/modifySimPixelTrackConfig.py "temp_cfg.py" ${CONFIGNAME}

# delete the temporary config
rm temp_cfg.py

echo "created config file ${CONFIGNAME}_SIM_cfg.py"
echo "procModifiers: ${PROCMODIFIERS}"
echo "customizations: ${CUSTOMIZE}"