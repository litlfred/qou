---
# qou-cvu9
title: 'Prior-Art Consolidated DOI-Verified Package: Ch.1 CQM/DHR, Ch.2 O_q(SU(2)) Geometry, & Remaining qou-tt2u Bibs (Owner OK Before PR)'
status: in-progress
type: task
priority: high
tags:
    - needs-owner-ok
created_at: 2026-11-23T21:31:07Z
updated_at: 2026-11-24T08:06:21Z
parent: qou-s028
---

Related beans: qou-tt2u, qou-hfwb, qou-awxv, qou-nq4h.
Verify EVERY citation DOI before adding (including the 7 refs added in #9180 commit e9c9fdafbe5 + Kadison & Jones 1983), list all authors for <=5-author papers (qou-nq4h), and prepare ONE consolidated prior-art package for owner OK before opening PR:
1. Ch. 1 CQM/DHR positioning: audit #9180 paragraph (Doplicher-Haag-Roberts 1971, Doplicher-Roberts 1989, Fredenhagen-Rehren-Schroer 1989, Frohlich-Gabbiani 1990, Coecke-Pavlovic-Vicary 2013) and add DOI-verified Abramsky-Coecke (2004) & Selinger (2007). STRICT NON-CLAIMS: QOU Frobenius object is finite rank; m_p/m_e is the q_0 pin (not an output); binding magnitude is open; Bring generation count is not established.
2. Ch. 2 O_q(SU(2)) geometry precedent: DOI-verify and position Larson-Sweedler (1969), Lin, Woronowicz (1987, 1989; closes qou-hfwb), Van Daele, Abramsky-Heunen (2012), Podles (1987), Brzezinski-Majid (1993), O Buachalla, Majid, Landi-Zampini, Chakraborty-Pal, Dabrowski-Landi-Sitarz-van Suijlekom-Varilly. Explicitly note Woronowicz's modular automorphism is NOT the tower's Nakayama twist (the tower has nu = id); keep novelty claims modest.
3. Remaining qou-tt2u bibliography entries: DOI-verified Saavedra Rivano, Greenberg, Han-Nambu, Tanaka, Webster, Hermann, Flapan + remaining qou-tt2u children (qou-dy2z, qou-d4hq, qou-9ehj, qou-3dh1, qou-8jd0, qou-6pns, qou-t7de).
Gate: present verified bibliography + diff summary and obtain owner OK before opening/merging PR.


2026-11-23 (Worker 24): Prepared and pushed consolidated DOI-verified prior-art package on branch `claude/prior-art-doi-verified-pkg-20261123` (commit `63446514c77`). DO NOT OPEN PR until explicit owner OK:
- Verified 50/50 DOIs live against `api.crossref.org` and `doi.org/api/handles/` (`responseCode == 1` on all 50; zbMATH `0331.53025` HTTP 200 for `tanaka1975`).
- Updated 14 existing `folio/references/*.json` entries (the 7 unverified `#9180` refs + `larson-sweedler1969`, `woronowicz1988`, `woronowicz1989`, `gunaydin-gursey1973`, `finkelstein2008`, `dubois-violette-todorov2018`, `todorov2018`) and added 34 new DOI-verified entries.
- Wired Ch. 0/1 CQM/DHR (`abramsky-coecke2004`, `selinger2007`) and all 4 non-claims in `intro-particles-as-knots.md`; Ch. 2 `O_q(SU(2))` geometry precedent + explicit `nu = id` vs Woronowicz modular automorphism distinction in `substrate-preamble.md` and `categorical-dirac-operator-intro.md`; `-- Ref:` keys in `CalculusDimensionObstruction.lean`, `SelfDualityDegree.lean`, `TwistedFrobeniusTower.lean`, `JonesIndexConventionD.lean` (`lean-direct-cone -j 1` green); and remaining `qou-tt2u` items (`qou-dy2z`, `qou-d4hq`, `qou-9ehj`, `qou-3dh1`, `qou-8jd0`, `qou-6pns`, `qou-t7de`).
- Gates: `check-references-bib` exit 0; `run-validate-references` 0 errors; `qa-sweep --ci` exit 0 (0 critical, 0 new major, 0 minor); `paper-commentary-audit` 0 fail / 0 advisory. Ready for owner OK to open PR.
