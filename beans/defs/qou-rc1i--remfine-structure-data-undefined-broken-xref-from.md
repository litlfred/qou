---
# qou-rc1i
title: rem:fine-structure-data undefined — broken xref from meson-em-sinh-closed-form
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T10:39:23Z
updated_at: 2026-11-15T14:10:00Z
parent: qou-mub3
---

run-validate warning 2026-08-07: content block meson-em-sinh-closed-form cross-references rem:fine-structure-data in its .md, but no block declares that label. Either the remark was renamed/removed and the reference not updated, or it was never authored. Fix: grep the corpus for the intended target (likely an alpha_EM / fine-structure data block) and repoint, or author the missing remark. Small, self-contained.

DONE 2026-11-15: already fixed on main 0d4e4a005e. rem:fine-structure-data is no longer referenced anywhere in folio/.
