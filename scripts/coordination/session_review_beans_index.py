"""W6 session review, step 3: index the mounted beans by PR / branch / session references.
Usage: python3 scripts/coordination/session_review_beans_index.py <workdir>  (run from repo root, beans mounted)."""
import os,re,json,sys
S=sys.argv[1]; d='beans/defs'; out={}
for f in os.listdir(d):
    t=open(os.path.join(d,f),errors='replace').read()
    fm=t.split('---')[1] if t.startswith('---') else ''
    def g(k):
        m=re.search(rf'^{k}:\s*(.*)$',fm,re.M); return m.group(1).strip() if m else None
    bid=f.split('--')[0].removesuffix('.md')
    out[bid]={'file':f,'title':(g('title') or '').strip("'\""),'status':g('status'),'type':g('type'),'parent':g('parent'),'updated':g('updated_at'),'pr':g('pr'),
      'prs':sorted(set(int(x) for x in re.findall(r'(?:#|pull/|PR\s?)(\d{3,5})\b',t))),
      'branches':sorted(set(re.findall(r'claude/[A-Za-z0-9._/-]+?-20\d\d-\d\d-\d\d',t))),
      'sessions':sorted(set(re.findall(r'(session_[A-Za-z0-9]{20,})',t)))}
json.dump(out,open(S+'/beans.json','w'))
print(len(out))
