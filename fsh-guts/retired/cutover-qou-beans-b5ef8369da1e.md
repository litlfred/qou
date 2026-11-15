---
$schema: folio-fsh-guts/v1
title: "beans/ of qou, as removed from main by its cutover"
kind: cutover-snapshot
movedOn: 2026-11-15
movedFrom: "beans/"
reason: cutover
instance: "qou"
directory: "beans"
sourceCommit: 490ab5c324181d0e00b4db64f2d18a5b7d6dc013
tree: b5ef8369da1e328c39c2abc7fd12d9b000d63fd3
authoritativeBranch: "cat/cat-harness/beans"
archive: "cutover-qou-beans-b5ef8369da1e.tar.gz"
files: 5660
bytes: 26134819
summary: >-
  beans/ as main tracked it at 490ab5c32418 (tree b5ef8369da1e, 5660 file(s),
  26134819 bytes), packed beside this file as cutover-qou-beans-b5ef8369da1e.tar.gz by git archive. It was removed from
  main by state:seed --cutover after cat/cat-harness/beans was verified authoritative and
  byte-identical; that branch is the live store, and this is the copy main last held.
---

# beans/ of qou, at its cutover

`cutover-qou-beans-b5ef8369da1e.tar.gz` beside this file holds `beans/` exactly as `main` tracked it at
`490ab5c324181d0e00b4db64f2d18a5b7d6dc013` — list it with `tar -tzf cutover-qou-beans-b5ef8369da1e.tar.gz`. Extracted and added to a
fresh index it writes tree `b5ef8369da1e328c39c2abc7fd12d9b000d63fd3`, which is how the cutover verified it before
removing anything.

The live content is on `cat/cat-harness/beans`, mounted at `beans/` by `state:mount`.
Do not unpack this back onto `main`: edit the branch.
