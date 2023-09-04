#!/usr/bin/env python3
#/home/yoxara/smodels/SmodelSSMS/2MDM/xsecH2.py

base_path = "/home/yoxara/smodels/SmodelSSMS/2MDM"
file_path = f"{base_path}/scripts/sigmaH2.txt"

MH2_values = list(range(250, 4000, 250))
Sa_values = [0.005,0.05, 0.1, 0.5]

with open(file_path, "w") as f:
    f.write(f"import {base_path}/Feynrules/2MDM/2MDM -modelname\n")
    f.write("define p = g u c d s b u~ c~ d~ s~ b~\n")
    f.write("generate p p > h2\n")
    f.write(f"output sigmaH2\n")
    f.write(f"launch sigmaH2\n")
    f.write("analysis = MadAnalysis4\n")
    f.write("set run_card nevents 15000\n")
    f.write("set run_card ebeam1 6500\n")
    f.write("set run_card ebeam2 6500\n")
    f.write("set run_card lpp1 1\n")
    f.write("set run_card lpp2 1\n")    
    f.write("set run_card pdlabel lhapdf\n")
    f.write("set run_card lhaid 303600\n")
    f.write("set run_card scale 91.188\n")
    f.write("set run_card dsqrt_q2fact1 91.188\n")
    f.write("set run_card dsqrt_q2fact2 91.188\n")
    f.write("set run_card scalefact 1.0\n")    
    f.write("set run_card nhel 0\n")
    f.write("set run_card sde_strategy 2\n")    
    f.write("set run_card bwcutoff 15.0\n")    
    f.write("set run_card maxjetflavor 5\n")
    f.write("set param_card gZp 1\n")

    for i in MH2_values:
        for j in Sa_values:
            f.write(f"set param_card MH2 {i}\n")
            f.write(f"set param_card Sa {j}\n")
            f.write("done\n")
            if i !=  MH2_values[-1] or j != Sa_values[-1] :
                f.write("launch\n")

    f.write(f"launch sigmaH2 -i\n")
    f.write(f"print_results --path={base_path}/data/sigmaH2.txt --format=short\n")
    f.write("exit\n")