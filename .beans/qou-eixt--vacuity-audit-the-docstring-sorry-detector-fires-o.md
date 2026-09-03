---
# qou-eixt
title: 'vacuity audit: the docstring-sorry detector fires on its own corrections'
status: completed
type: task
priority: normal
created_at: 2026-09-03T12:44:06Z
updated_at: 2026-09-03T15:12:34Z
---

MEASURED on main b8d883189d.

THE DEFECT. proof-docstring-sorry-mismatch fires on a docstring that QUOTES the wording it replaced. This corpus's house style, when a docstring is corrected, is to quote the superseded text -- 'the paragraph that stood here said ...', 'Until 2026-08-08 this docstring said ...', 'the previous wording called this ...'. The quoted sentence still carries a present-tense sorry claim, so the detector fires on the CORRECTION and keeps firing forever. A permanent false positive that grows every time someone does the right thing.

Of the 5 findings live on that commit, FOUR were this shape. Only shell_filling_rule was anything else (genuine delegation whose DOC_DELEGATES_SORRY exemption needs fileHasSorry, which is false there).

TWO CORRECTIONS TO MY OWN EARLIER CLAIMS, both stated in PR #6471 and its bean and both wrong:
  1. I said the detector 'cannot tell a docstring that truthfully says this is NOT a sorry'. FALSE -- 'not\s+a\s+sorry' was ALREADY in SORRY_MENTION_IS_HISTORICAL. Negation was handled all along.
  2. I said 'two of my own corrections still fire'. FALSE -- only ONE is mine (confinement_categorical). nucleon_ordering_factorization fires on a pre-existing header ('Honest sorry -- and now actually one.') that I appended below; it was already firing before I touched the file.
Both errors came from inferring the mechanism from the count instead of extracting the triggering sentence. Extracting it took one script.

Near-miss worth recording: the regex had 'previously' but not 'previous', so 'the previous wording' slipped through on a suffix.

FIX. SORRY_MENTION_QUOTES_SUPERSEDED, a second regex kept separate from the historical one so the two can be measured apart, consumed by a new docstringSorryIsHistorical() helper. Patterns: previous (wording|version|revision|encoding|paragraph|sentence|docstring), (stood|read) here, (docstring|wording|sentence|paragraph|header|note) (said|read|called|claimed), earlier revision, until YYYY-MM-DD.

Result 5 -> 1. The survivor is shell_filling_rule, correctly still flagged.

GUARDED. --selftest-docstring-sorry, 12 fixtures, ALL REAL CORPUS TEXT: the 4 superseded-text quotes must be suppressed, and the 8 genuine mismatches drained in PR #6471 must STILL fire. The risk of these patterns is over-suppression, so the second half is the important half. NEGATIVE CONTROL RUN: adding 'honest' to the pattern makes the selftest fail with 3 named fixtures and exit 1; restoring makes it green. The guard is not merely present, it bites.
