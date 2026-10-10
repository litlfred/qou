---
# qou-3s5e
title: Does the rational-twist quantisation have any discriminating power?
status: completed
type: task
priority: normal
created_at: 2026-09-02T21:25:31Z
updated_at: 2026-09-02T21:28:59Z
---


RESOLVED 2026-09-02 -- computations/probes/the_twist_is_absent_where_it_is_needed_probe.py,
6/6. This probe tests a claim of MINE (qou-bq9l) and fails it, twice. The net
result reverses that bean's conclusion.

CORRECTION 1 -- THE CUMULATIVE SET IS DENSE, SO THE PREDICTION IS VACUOUS.
Union of achievable t over n up to a cutoff, against the 45 rationals in (0,1)
with denominator <= 12:
    n<= 5:   1 distinct t    2 %
    n<= 8:   4               9 %
    n<=12:  13              29 %
    n<=16:  32              51 %
    n<=20:  57              69 %
    n<=24:  86              96 %   (43 of 45; only 4/9 and 7/8 missing)
Eight exact group-theoretic ratios -- QCD 3bar/6 = 2, QCD singlet/octet = 8,
piN at the Delta 9 and 9/2, quark-model |mu_p/mu_n| = 3/2 and g_A = 5/3, 4, and
SU(6) 25/9 -- ALL EIGHT HIT. A test everything passes is not a test. qou-bq9l's
n<=12 table looked sparse only because of where it was cut.

CORRECTION 2 -- CUMULATIVE WAS THE WRONG OBJECT. A physical system has a FIXED
strand count: two quarks are n=2, a nucleon n=3, two nucleons n=6, 4He n=12. Per
n the sets are SMALL:
    n    A    admissible t in (0,1)                       count
    3    1    NONE                                            0
    6    2    NONE                                            0
    9    3    2/9, 2/3, 8/9                                   3
   12    4    1/3, 1/2, 2/3                                   3
   15    5    2/15, 4/15, 2/5, 2/3, 4/5, 14/15                6
   18    6    1/9, 2/9, 1/3, 5/9, 2/3, 7/9, 8/9               7
So the quantisation IS sharply constraining -- just not in the form qou-bq9l
stated it.

THE DECISIVE FACT: NOTHING AT THE STRAND COUNTS THAT MATTER. t in (0,1) needs
c(lambda) strictly between -n/2 and 0.
  n=6: achievable content sums {-15,-9,-5,-3,0,3,5,9,15}; window needs {-1,-2}.
       NEITHER EXISTS.
  n=3: window needs {-1}; does not exist.
  n=2: only c=-1, giving t = 1 EXACTLY -- the excluded boundary where the T=0
       channel unbinds and the ratio diverges.

CONSEQUENCES:
 * THE TWO-NUCLEON SECTOR CANNOT BE REPAIRED BY THIS MECHANISM. It is n=6, it is
   where qou-v3u2 proved the impossibility lives, and it admits no admissible
   twist at all.
 * THE t = 1/3 QCD HIT IS WITHDRAWN AS EVIDENCE. It is realised at n=12, but two
   quarks are n=2, which offers only the excluded boundary. A colour observable
   for 3(x)3 cannot be evaluated at 4He's strand count.

WHAT SURVIVES OF qou-bq9l: the mechanism itself -- c_n^n = Delta^2, block
magnitude exactly q^(2c(lambda)/n), fractionality from n=5 -- and the per-n
availability table as a sparse, closed-form, falsifiable structure. Forward
pointer added to that probe's docstring.

NET: the missing ingredient was correctly identified (qou-vlrq), and the
substrate does not supply it where it is needed.

CAVEAT ON THE CORRECTION ITSELF: the per-n analysis assumes a system's twist
must come from its OWN strand count. That is the natural reading -- the Coxeter
element of B_n is defined on n strands -- but a construction could embed a
subsystem in a larger braid and inherit a twist from there. Nothing here rules
that out; it would need the embedding exhibited, and the resulting object would
no longer be the n-strand system's own Coxeter element.
