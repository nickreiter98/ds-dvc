# Initialize DVC Examen
```bash
dvc init #create local DVC control
dvc add 'filename' #add to DVC cache
dvc commit #record changes to a file already tracked by DVC
dvc push #push changes  

dvc stage add -n 'name' -d 'dependant' -o 'output' python 'main script'
dvc repro #trigger pipeline
dvc repro 'step name' #trigger only specific step
```
