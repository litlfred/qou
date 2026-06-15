#!/usr/bin/env python3
"""
Build nuclei A=1..10 using pruned Hecke reduction.

After each Hopf link + reduce step, prune terms with |coeff| < threshold.
This prevents OOM while preserving dominant structure.

Then CHECK: is every word in the support a valid reduced word?
  1. No σ_i σ_i (Hecke reducible)
  2. No σ_i σ_{i+1} σ_i > σ_{i+1} σ_i σ_{i+1} in lex order (YB reducible)
  3. No σ_i σ_j with i > j and |i-j| >= 2 (far-comm reducible)

If any word fails → NOT in normal form → FAIL.

Usage:
    python3 pruned-normal-forms.py
"""

import math
import time
from q_parameter import Q as q, Q_INV as qi
from hecke_division import HeckeDivision, HeckeElement

div = HeckeDivision(q_val=q)

PRUNE_THRESHOLD = 1e-6  # keep terms with |coeff| > this
MAX_TERMS = 5000        # hard cap on term count

def prune(elem, threshold=PRUNE_THRESHOLD, max_terms=MAX_TERMS):
    """Remove small terms to prevent blowup."""
    if elem.n_terms() <= max_terms:
        return elem
    # Sort by |coeff| descending, keep top max_terms
    sorted_terms = sorted(elem.terms.items(), key=lambda x: -abs(x[1]))
    kept = {w: c for w, c in sorted_terms[:max_terms] if abs(c) > threshold}
    return HeckeElement(kept)

def is_reduced_word(word):
    """Check if a word is in Gröbner--Shirshov normal form.

    Returns (True, None) if reduced, (False, reason) if not.
    """
    for pos in range(len(word) - 1):
        # Rule 1: No σ_i σ_i (Hecke reducible)
        if word[pos] == word[pos + 1]:
            return False, f"Hecke: sigma_{word[pos]}^2 at pos {pos}"

        # Rule 3: Far-comm — σ_i σ_j with i > j, |i-j| >= 2
        if abs(word[pos] - word[pos+1]) >= 2 and word[pos] > word[pos+1]:
            return False, f"far-comm: sigma_{word[pos]} sigma_{word[pos+1]} at pos {pos}"

    # Rule 2: YB — σ_i σ_{i+1} σ_i where (i,i+1,i) > (i+1,i,i+1) in lex
    for pos in range(len(word) - 2):
        a, b, c = word[pos], word[pos+1], word[pos+2]
        if a == c and abs(a - b) == 1:
            new_trip = (b, a, b)
            old_trip = (a, b, a)
            if old_trip > new_trip:
                return False, f"YB: sigma_{a} sigma_{b} sigma_{a} at pos {pos}"

    return True, None

def check_normal_form(elem):
    """Check ALL words in the element's support."""
    n_words = len(elem.terms)
    n_fail = 0
    failures = []
    for word in elem.terms:
        ok, reason = is_reduced_word(word)
        if not ok:
            n_fail += 1
            if len(failures) < 5:  # only show first 5
                ws = '.'.join(f's{i}' for i in word)
                failures.append(f"  {ws}: {reason}")
    return n_fail, n_words, failures

# ── Build A=1..10 ───────────────────────────────────────────────

sequence_pnpn = []  # alternating p,n
def get_sequence(A):
    seq = []
    pi, ni = 0, 0
    # target: roughly equal p and n, alternating
    p_target = (A + 1) // 2
    n_target = A - p_target
    for k in range(A):
        if pi < p_target and (ni >= n_target or k % 2 == 0):
            seq.append('p'); pi += 1
        else:
            seq.append('n'); ni += 1
    return seq

print(f"Pruned normal forms for A=1..10")
print(f"q = {q:.6f}, prune threshold = {PRUNE_THRESHOLD}, max terms = {MAX_TERMS}")
print()

elem = HeckeElement.identity()
sequence = []

for A in range(1, 11):
    # Determine next nucleon
    full_seq = get_sequence(A)
    ntype = full_seq[A-1]
    sequence.append(ntype)

    p_count = sum(1 for t in sequence if t == 'p')
    n_count = sum(1 for t in sequence if t == 'n')

    t0 = time.time()

    if A == 1:
        pass  # elem = identity, already set
    else:
        # Add crossings with all prior nucleons
        for j in range(A - 1):
            jtype = sequence[j]
            if jtype == 'p' and ntype == 'p':
                cx = div.crossing_positive(j)
            elif jtype == 'n' and ntype == 'n':
                cx = div.crossing_negative(j)
            else:
                cx = div.crossing_mixed(j)
            elem = elem * cx

        # Reduce
        elem, _ = div.reduce(elem)

        # Prune if needed
        before_prune = elem.n_terms()
        elem = prune(elem)
        after_prune = elem.n_terms()
        pruned = before_prune - after_prune

    elapsed = time.time() - t0

    # Check normal form
    n_fail, n_words, failures = check_normal_form(elem)

    # Dominant term
    dom_word, dom_coeff = elem.dominant_term()
    if dom_word is not None:
        dom_str = '.'.join(f's{i}' for i in dom_word) if dom_word else '1'
        dom_len = len(dom_word)
    else:
        dom_str = '(empty)'
        dom_len = 0
        dom_coeff = 0

    # Word length histogram
    hist = elem.word_histogram()

    # Status
    status = "OK" if n_fail == 0 else f"FAIL ({n_fail}/{n_words})"

    print(f"A={A:>2} N({p_count},{n_count}) seq={''.join(sequence):>10s} | "
          f"{n_words:>5} terms | "
          f"dominant: {dom_coeff:>8.4f} x {dom_str} (len {dom_len}) | "
          f"NF: {status} | {elapsed:.2f}s")

    if A > 1 and before_prune != after_prune:
        print(f"     pruned {before_prune} -> {after_prune} terms")

    if n_fail > 0:
        print(f"     FAILURES:")
        for f in failures:
            print(f"       {f}")

    # Show histogram
    hist_str = ' '.join(f'L{k}:{v}' for k, v in sorted(hist.items()))
    print(f"     histogram: {hist_str}")

    # Show top 3 terms
    top3 = sorted(elem.terms.items(), key=lambda x: -abs(x[1]))[:3]
    for w, c in top3:
        ws = '.'.join(f's{i}' for i in w) if w else '1'
        print(f"     top: {c:>+10.6f} x {ws}")

    print()
