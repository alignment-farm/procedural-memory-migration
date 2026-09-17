"""Cache copied provenance and versioned methods; no arXiv metadata requests."""
import hashlib,json,pathlib,shutil,subprocess,urllib.request
root=pathlib.Path(__file__).resolve().parents[1]
src=root/'sources'; src.mkdir(exist_ok=True)
up=root/'../../construct-2/sources/2026-09-17-independent-study-selection'
manifest=[]
for name in ['README.md','retrieval.json','selected-metadata.xml','upgrade-metadata.xml','memcollab-metadata.xml','artifact-inspection.json']:
    target=src/('upstream-'+name); shutil.copyfile(up/name,target)
    manifest.append({'file':target.name,'origin':str(up/name),'upstream_revision':subprocess.check_output(['git','-C',str(up),'rev-parse','HEAD'],text=True).strip(),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
for paper in ['2608.22533v1','2609.05339v1']:
    url='https://arxiv.org/html/'+paper
    request=urllib.request.Request(url,headers={'User-Agent':'ProceduralMemoryMigrationStudy/0.1 (bounded methods inspection; local reproducibility archive)'})
    with urllib.request.urlopen(request,timeout=60) as response: data=response.read()
    target=src/(paper+'.html'); target.write_bytes(data)
    manifest.append({'file':target.name,'url':url,'sha256':hashlib.sha256(data).hexdigest()})
(src/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
