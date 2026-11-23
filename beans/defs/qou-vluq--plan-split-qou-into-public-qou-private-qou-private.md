---
# qou-vluq
title: 'Plan: split qou into public qou + private qou-private (library PDFs)'
status: todo
type: feature
priority: normal
created_at: 2026-11-23T21:44:05Z
updated_at: 2026-11-23T22:04:09Z
parent: qou-5bkr
---

Owner request 2026-11-23: move library PDFs to private repo litlfred/qou-private (same as qou, stays private). Plan doc: https://claude.ai/artifact/3njuXb33bTdSonhSnFJAED
Key fact: PDFs (820 on main, 728 MB, 872 ever added) and extracted full text (sections/, ocr/, ~94k files) are in history on all 8,849 branches, so deleting on main is not enough; history rewrite (git filter-repo) or fresh public repo needed. GitHub forks of public repos cannot be private, so qou-private = private mirror with qou as upstream.
Steps: 1 mirror-push qou to qou-private; 2 choose removed paths; 3 filter-repo; 4 trim public branches; 5 point corpus-grep path 5 + ingest at qou-private; 6 sync; 7 scans then go public on owner word.
Needs: access to qou-private in the environment; owner decisions 1-4 in the doc. Nothing public yet (owner).

2026-11-23 21:55Z: backup step 1 PARTIAL. main (53e92f765e, full history incl. library PDFs) pushed to qou-private. Other 7,864 branches + 3 tags: push refused by this session's git proxy (HTTP 403, branch policy), so the owner pushes them from their machine:
cd ~/space_cats && git clone --mirror https://github.com/litlfred/qou qou-mirror.git && cd qou-mirror.git && git push https://github.com/litlfred/qou-private 'refs/heads/*:refs/heads/*' 'refs/tags/*:refs/tags/*'
(mirror is 16 GB).
