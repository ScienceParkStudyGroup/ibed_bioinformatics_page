# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
mamba create --name snakemake_f_NanoITS -c conda-forge -c bioconda snakemake=7.32.4 python=3.11.6 tabulate=0.8

cd <path_to_install_software>
git clone https://github.com/ndombrowski/NanoITS.git
mv NanoITS/ NanoITS_0.3
#
#
#
#
#
#
#
#
#
conda activate snakemake_f_NanoITS

snakemake --use-conda --cores <nr_cores> \
  -s <path_to_NanoITS_install>/workflow/Snakefile \
  --configfile config/config.yaml \
  --conda-prefix <path_to_NanoITS_install>/workflow/.snakemake/conda  \
  --rerun-incomplete --nolock 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
