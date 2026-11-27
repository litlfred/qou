import json,sys,collections,re
S,OUT=sys.argv[1],sys.argv[2]
rows=json.load(open(S+'/rows2.json')); beans=json.load(open(S+'/beans.json'))
prs={int(k):v for k,v in json.load(open(S+'/prs_slim.json')).items()}
BOGUS='session_01E667391F74184786BF4B9D'
BAD={BOGUS,'session_01R46Ni4bTqcpColourTowerCP','session_01TQPEQfnjRHW41uyJXCbdjXq','session_033bc8ed','session_8c64c5f1'}
COORD_NOW='session_01VQDpPdnjTBLBcPi6D5gj61'; PARENT='session_01AgoHcE'
TARGET={8523,8522,8365,8521,8082,8098,8100,7610,7440,7443,8367,8517,8502,8126,7876,8064,8374,8526}
def keep_reason(r):
    s=r['session']
    if s==COORD_NOW: return 'live coordinator / merge manager'
    if s.startswith(PARENT): return 'parent coordinator of the 01Qmmkt*/0151ZZJ* children that still own first-target PRs; archive after them'
    tp=[n for n in r['prs_open'] if n in TARGET]
    if tp and (r['last'] or '')>='2026-11-15': return 'owns first-target PR(s) '+', '.join('#%d'%n for n in tp)+' still in W1–W3 review; its context answers review comments'
    if (r['last'] or '')>='2026-11-18': return 'active on/after 2026-11-18; may still be running'
    return None
for r in rows: r['keep_open']=keep_reason(r) if r['session'] not in BAD else None
real=[r for r in rows if r['session'] not in BAD]
# items dedup
items={}
for r in real+[x for x in rows if x['session'] in BAD]:
    for i in r['items']:
        k=(i['kind'],i['id'])
        if k not in items: items[k]=dict(i,origin=[])
        items[k]['origin'].append(r['short'])
WS=['W1','W2','W3','W4','W5','COORD','NEW-H','NEW-R','NEW-P']
def bean_parent(b):
    p=beans[b]['parent']; return p
L=[]
a=L.append
cls=collections.Counter(r['class'].split()[0] for r in real)
a('# Session review (W6) — 2026-11-20\n')
a('Workstream W6 of the coordinator plan (epic `qou-c20n`). Finds the outstanding work left by older Claude sessions on `litlfred/qou`, routes it to W1–W5 (or proposes a new owner), and lists which sessions the owner can archive. **Nothing here archives, closes, merges or re-scopes anything**; the archive action is the owner\'s.\n')
a('## How this was measured\n')
a('- **Sessions** = distinct `claude.ai/code/session_…` ids in commit messages on `origin/main` (head `917b6939954`, full history back to the shallow boundary 2026-06-09: 25,232 commits, 18,536 carrying a trailer) plus every id linked from a PR body or carried by an unmerged PR\'s commits. Command: `git log origin/main --format=\'%x1e%H%x09%ci%x09%s%n%b\'`, grouped by trailer.')
a('- **PRs**: all 6,600 PRs created since 2026-05-31 via REST `pulls?state=all` (5,850 merged, 412 open, 338 closed unmerged); commits of the 750 unmerged ones via `pulls/<n>/commits` for their trailers.')
a('- **Beans**: the mounted tracker (`beans/defs/`, 5,793 files: 3,210 completed, 1,813 in-progress, 402 todo, 336 scrapped). A bean is tied to a session when it names the session id, has `pr:` equal to one of the session\'s PRs, names one of its PR branches, or its id appears in one of its PR titles/branches.')
a('- **Classification**: HAS-OUTSTANDING-WORK = the session has an open PR or an open (todo/in-progress) bean tied to it that is not merely a close-candidate; SUPERSEDED-BY = its only PRs were closed unmerged and a later merged/open PR cites each; COMPLETE = otherwise.')
a('- **Limits, stated plainly.** (1) Work that was never pushed is invisible here: a session that stopped with uncommitted work looks COMPLETE. (2) The bean↔PR join partly uses `#N` mentions in bean bodies, so a bean can be over-attributed to a session whose PR it merely cites. (3) Research-open vs mechanical is a keyword heuristic on titles; treat it as a sort key, not a verdict. (4) Pre-2026-06-09 history was not fetched.\n')
a('## claude.ai chats\n')
a('`mcp__claude_ai__recent_chats` and `conversation_search` are **not available in this session** (not in the tool list, and `ToolSearch` finds no match). The predecessor W6 run had them and reported that every query returned **nothing** from a Project-bound session. So claude.ai chat conversations were **not reviewed**; only Claude Code sessions that left commits or PRs are covered. If the owner wants chats reviewed, that needs a session started outside the Project.\n')
a('## Result\n')
a('| class | sessions |\n|---|---:|')
for k in ['COMPLETE','HAS-OUTSTANDING-WORK','SUPERSEDED-BY']: a(f'| {k} | {cls[k]} |')
a(f'| total (real ids) | {len(real)} |\n')
a('**Ids that are not real sessions** (excluded from both archive lists; their items are still routed):\n')
a(f'- `{BOGUS}` — 24 hex characters, linked from 51 open batch PRs (W4). Not a Claude session id.')
a('- `session_01R46Ni4bTqcpColourTowerCP` (#8139), `session_01TQPEQfnjRHW41uyJXCbdjXq` (33 chars; looks like a mistyped `01TQPEQf…`), `session_033bc8ed`, `session_8c64c5f1` — malformed ids written by hand into a PR body or trailer.')
a('- `session_0151ZZJzC6MYcwqpYVZci9h6` (2 PR bodies: #8522, #8523) and `session_0151ZZJzCWMYcwqpYVZci9h6` (commit trailer) differ in one character; one is a copying error. Both are kept in KEEP OPEN until the owner sees which link opens.\n')
keep=[r for r in real if r['keep_open']]; safe=[r for r in real if not r['keep_open']]
a(f'Archive: **{len(safe)} SAFE TO ARCHIVE**, **{len(keep)} KEEP OPEN** (lists at the end). "Safe" means every outstanding item the session left is now carried by an open PR or a bean routed below, so closing the transcript loses no tracked work. It does not mean the work is done.\n')
cnt=collections.Counter((i['ws'],i['kind'],i['class']) for i in items.values())
a('### Outstanding items by owner\n')
a('| owner | open PRs | beans: research-open | beans: mechanical |\n|---|---:|---:|---:|')
for w in WS:
    a(f"| {w} | {sum(v for (x,k,c),v in cnt.items() if x==w and k=='pr')} | {cnt[(w,'bean','research-open')]} | {cnt[(w,'bean','mechanical')]} |")
a('\nOwners: W1 mass proof (Lean) · W2 mass/binding compute & precision · W3 photon/QED · W4 batch Lean PR triage · W5 legacy `claude/*` PR triage & ports · COORD coordinator. **Proposed new owners**: NEW-H, NEW-R, NEW-P (see below).\n')
a('## Coordinator family (01AgoHcE and children)\n')
fam=[r for r in real if r['session'].startswith(PARENT) or r['parent']]
a(f'{len(fam)} sessions: the coordinator `01AgoHcE` and its `01Qmmkt*` / `0151ZZJ*` children (2026-11-15…19). Every open PR they left is in the routing tables below; the five W1–W3 first-target owners stay open.\n')
a('| session | dates | main commits | open PRs | class |\n|---|---|---:|---|---|')
for r in sorted(fam,key=lambda r:r['session']):
    a(f"| [{r['short']}]({r['url']}) | {r['first']}→{r['last']} | {r['main_commits']} | {', '.join('#%d'%n for n in r['prs_open']) or '—'} | {r['class']} |")
a('')
a('## Outstanding work, routed\n')
def origin(i): return ', '.join(sorted(set(i['origin'])))[:80]
for w in WS:
    pr_i=sorted([i for i in items.values() if i['ws']==w and i['kind']=='pr'],key=lambda i:-i['id'])
    b_i=sorted([i for i in items.values() if i['ws']==w and i['kind']=='bean'],key=lambda i:(i['class'],i['id']))
    if not pr_i and not b_i: continue
    a(f'### {w}\n')
    if w=='W4':
        a(f'W4 owns all ~333 batch PRs regardless of session; listed here are only the {len(pr_i)} batch/feat PRs whose commits or body carry a real session id, and the {len(b_i)} beans those PRs implement. Full list in the JSON (`items`). Beans by parent epic:\n')
        pc=collections.Counter(beans[i['id']]['parent'] or '—' for i in b_i)
        a('| parent epic | beans |\n|---|---:|')
        for p,n in pc.most_common(15): a(f'| `{p}` | {n} |')
        a('')
        continue
    if pr_i:
        a('| PR | title | class | from session |\n|---|---|---|---|')
        for i in pr_i: a(f"| #{i['id']} | {i['title'][:90].replace('|','/')} | {i['class']} | {origin(i)} |")
        a('')
    if b_i:
        a('| bean | status | title | class | from session |\n|---|---|---|---|---|')
        for i in b_i: a(f"| `{i['id']}` | {i['status']} | {i['title'][:90].replace('|','/')} | {i['class']} | {origin(i)} |")
        a('')
a('## Proposed new owners\n')
a('- **NEW-H — bean ledger hygiene** (mechanical, owner-gated). The NEW-H beans are `in-progress` but every PR they reference is merged and none is open: most are finished work whose bean was never closed. Closing them is a sweep, so under §ASK-OWNER it is a decision, not something W6 did. Parent: epic `qou-w3yy` (bean tracker hygiene). Tracking bean created by this run (see below).')
a('- **NEW-R — research/Lean backlog with no PR** . Open beans from older sessions that no current PR implements and whose topic is not mass, compute or photon (topology, Bring, Hecke foundations, fluid dynamics …). They need an owner priority call, not a workstream; until then they stay where they are.')
a('- **NEW-P — platform and agent tooling** (milestone `qou-5vkl`): skills, agent memory, library ingestion, references split.\n')
a('## Decisions for the owner\n')
a('### D1. Close the NEW-H close-candidate beans?\n')
a('- **What it means:** set the listed `in-progress` beans to `completed` after a per-bean check that the merged PR really did the bean\'s task.')
a('- **Cost:** one pass over the listed beans (bodies are short); one beans-branch push.')
a('- **Risk:** a bean whose merged PR was only a partial step would be closed early; reversible (status edit), but the AGENTS rule "never close a bean whose subject is an open conjecture" applies, so research beans must be skipped by hand.')
a('- **Commits to:** nothing beyond those beans.')
a('- **Default if no answer:** nothing changes; the beans stay `in-progress` and keep inflating the 1,813 in-progress count.')
a('- **Recommendation (judgement):** yes, as a checked pass by whichever workstream owns hygiene, skipping any bean whose title names a conjecture, derivation or gap.\n')
a('### D2. Who owns NEW-R?\n')
a('- **What it means:** either (a) leave these beans unowned until a later tranche, or (b) add a W7 research-backlog workstream that ranks them.')
a('- **Cost:** (a) none; (b) one session.')
a('- **Risk:** (a) the beans keep aging; (b) attention moves off the mass chapter.')
a('- **Commits to:** (b) a seventh workstream.')
a('- **Default if no answer:** (a).')
a('- **Recommendation (judgement):** (a) until W1–W3 land their first targets.\n')
a('## Sessions with outstanding work or superseded\n')
a('| session | dates | main commits | open PRs | open beans | class |\n|---|---|---:|---|---:|---|')
for r in real:
    if r['class']=='COMPLETE': continue
    a(f"| [{r['short']}]({r['url']}) | {r['first']}→{r['last']} | {r['main_commits']} | {', '.join('#%d'%n for n in r['prs_open'][:6]) or '—'} | {sum(1 for i in r['items'] if i['kind']=='bean')} | {r['class']} |")
a('')
a('## KEEP OPEN\n')
for r in keep: a(f"- [{r['session']}]({r['url']}) — {r['keep_open']}")
a('\nAlso keep the live W1–W6 sessions of 2026-11-20 (their ids are not on main yet).\n')
a('## SAFE TO ARCHIVE\n')
a(f'{len(safe)} sessions, newest first. Class and last own activity in brackets; outstanding items, where any, are routed above.\n')
for r in safe: a(f"- [{r['session']}]({r['url']}) — {r['last']} · {r['class'].split(' ')[0]}" + (f" · {r['class'].split(' ',1)[1]}" if r['class'].startswith('SUPERSEDED') else ''))
open(OUT+'.md','w').write('\n'.join(L)+'\n')
json.dump({'schema':'qou-session-review/v1','generated':'2026-11-20','main_head':'917b6939954','method':'see .md §How this was measured',
  'chat_tools':'mcp__claude_ai__recent_chats / conversation_search not available in this session; predecessor reported empty results',
  'non_session_ids':sorted(BAD),'counts':dict(cls),'safe_to_archive':[r['session'] for r in safe],'keep_open':{r['session']:r['keep_open'] for r in keep},
  'sessions':rows,'items':sorted(items.values(),key=lambda i:(i['ws'],i['kind'],str(i['id'])))},open(OUT+'.json','w'),indent=1,ensure_ascii=False)
print(len(safe),len(keep),cnt)
