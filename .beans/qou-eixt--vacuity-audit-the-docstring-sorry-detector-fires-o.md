---
# qou-eixt
title: 'vacuity audit: the docstring-sorry detector fires on its own corrections'
status: completed
type: task
priority: normal
created_at: 2026-09-03T12:44:06Z
updated_at: 2026-09-04T02:18:05Z
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

MERGED 2026-09-04 as cf6146d66e (rebase, 7 linear commits on main). PR #6507.

WHAT LANDED, per criterion:
  proof-no-provable-axiom      2 -> 0   (ahlfors1979 cited on the surviving axiom;
                                         main proved the other mid-flight, e3051fb1df)
  proof-docstring-sorry-mismatch 5 -> 1 (SORRY_MENTION_QUOTES_SUPERSEDED +
                                         --selftest-docstring-sorry, 12 real fixtures)
  proof-claims-unencoded       6 -> 5   (the live q-beta carrier restated; the survivor
                                         at EigenphaseCarrierVacuity:70 is the deliberate
                                         demonstration copy and stays)

THE MERGE-METHOD STEP, worth recording because it nearly went wrong:
rule 8 defaults to rebase-merge, but the branch carried a merge commit (main had been
merged in to resolve a ledger conflict), and rebase-merge DROPS merge commits. Tested in
a scratch worktree rather than assumed: `git rebase origin/main` FAILED on the
axiom-citation commit, which cited both axioms and was being replayed against a main that
had since proved one. Resolved locally with the entry-union resolver (one trivial
updated_at hunk) and force-with-lease pushed. The check that made it safe: the rebased
tree hash is BYTE-IDENTICAL to the verified merge result (299ef22617 both sides), so the
verification transfers exactly rather than by argument.

CORRECTION TO MY OWN CLAIM, made twice before it was caught: I reported this branch
conflict-free on `git merge-tree <base> <ours> <theirs> | grep -c '^<<<<<<<'` returning 0.
That check MEASURES NOTHING -- the old three-argument form does not emit conflict markers
at line start, so it can only ever return 0. Use `git merge-tree --write-tree HEAD
origin/main` and read the EXIT CODE. The API's mergeable_state was also true-but-stale
(computed against a base 16 commits back). A real conflict was hiding behind both.
