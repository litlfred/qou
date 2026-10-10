---
# qou-hb5v
title: Migrate the lake-cache branch family to cat/folio-assistant-sci/lake-cache/ (declared in qou.json)
status: in-progress
type: task
created_at: 2026-10-05T15:07:33Z
updated_at: 2026-10-05T15:07:33Z
parent: qou-n4r9
---

Owner 2026-10-05: "migratez qou". qou.json declares the lake-cache family (storage.branchPrefix cat/folio-assistant-sci/lake-cache/, keyedBy family); scripts/lib/lake-cache-family.sh reads it. Writes go to the declared name; reads prefer it and fall back to legacy lake-cache/<member>. Legacy branches kept (AGENTS.md rule 9). Pin bumped to 483ed296b (family keying). Platform side: folio-assistant beans rva2 / j9cs, PR litlfred/folio-assistant#2192.

## Done when
- [x] qou.json declares the family; parses at the new pin, fails at the old one (measured)
- [x] six scripts + lake-cache-refresh.yml read the declaration
- [x] pin + build.yml bumped together; run-validate 6 -> 9 (3 new unlisted-block warnings, pre-existing state)
- [ ] PR merged on the owner's "merge it"
- [ ] first seed after merge creates a new-name branch (observed, not assumed)
