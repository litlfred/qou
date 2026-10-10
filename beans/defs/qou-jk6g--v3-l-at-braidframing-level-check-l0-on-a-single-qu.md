---
# qou-jk6g
title: 'V3: L at braid/framing level + check L=0 on a single quark'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T18:23:24Z
updated_at: 2026-10-04T15:25:22Z
parent: qou-8lxd
---

Follows LeptonNumberCarrierChirality.lean: L cannot factor through the UNFRAMED
knot type (mirror must move the carrier; unknot is amphichiral). Corpus already
works at braid level -- AntiparticleCrossingReversalContext's mirror is
sigma_i -> sigma_i^-1 on BRAID WORDS and records that the mirror preserves the
knot type. So define L on braid words / framed objects and check it returns 0 on
a single quark (the B-L = 1/3 quark row currently has nothing behind it -- the
corpus's L table lists only leptons, 'hadrons L=0' is prose).
BLOCKED BY V2: if L needs framing while Y needs framing-independence, they cannot
be the same datum.
