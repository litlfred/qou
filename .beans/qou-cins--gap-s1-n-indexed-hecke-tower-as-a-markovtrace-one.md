---
# qou-cins
title: 'GAP S1: N-indexed Hecke tower as a MarkovTrace -- one R-algebra with g:N->A + growing H, from the IwahoriHecke type-A tower'
status: todo
type: task
priority: normal
created_at: 2026-09-12T11:54:27Z
updated_at: 2026-09-12T11:54:28Z
---

Parent: qou-0fmb (arc), under epic qou-08a2. Build a single R-algebra A with g:N->A + growing H:N->Subalgebra matching OcneanuTrace.MarkovTrace's tower shape, from IwahoriHecke (Defn.IwahoriHecke over type-A Coxeter S_infinity, or a DirectLimit of Hecke K q qi n via BraidTower.braidTower). Must carry h=q-q^-1 != 0 at every generator (so a finite model padded with g_n=1 FAILS: quad forces h=0). This is why the instance needs a genuine infinite tower. Coset basis (qou-uoal, HeckeCoset.lean) is the free-module backbone. Sorry-free; lean-direct; bean the gap if the colimit fights.
