# Route 2, recipe R-q: results

q0 = 1.1099785827513808075916690956107688798744991218736 (proton pin). mpmath 60 dps. Recipe: preregistration-qdeformed.md. No ranking rule; nothing selected.

## Checks

- full_twist_is_t3_I: PASS
- classical_limit_matches_sl2z: PASS
- det_is_(-t)^n: PASS
- conjugate_pairs_equal_x: PASS

## Symbolic images (exact, in t)

- nuc9: tr = 0, det = -t**9
- nuc11_interleaved: tr = t**5*(t - 1), det = -t**11
- gluon_s0_s1: tr = t**5*(t - 1), det = -t**11
- gluon_s1_s0: tr = -t**4*(t - 1)*(t**2 + 1), det = -t**11
- gluon_s1_s1: tr = -t**4*(t - 1)*(t**2 + 1), det = -t**11
- gluon_s0_s0: tr = t**5*(t - 1), det = -t**11
- nuc11_gen_grouped: tr = -t*(t - 1)*(t**8 - t**7 + 2*t**6 - t**5 + 3*t**4 - t**3 + 2*t**2 - t + 1), det = -t**11

## t=+q0

| word | det | x = abs(tr)/sqrt(abs(det)) | type | length |
|---|---|---|---|---|
| nuc9 | -2.557592746943598482591003 | 0.0 | glide reflection | 0.0 |
| nuc11_interleaved | -3.151088420630975731134374 | 0.1043880582591816378331172 | glide reflection | 0.1043407203195195123159063 |
| gluon_s0_s1 | -3.151088420630975731134374 | 0.1043880582591816378331172 | glide reflection | 0.1043407203195195123159063 |
| gluon_s1_s0 | -3.151088420630975731134374 | 0.209913619275028895066292 | glide reflection | 0.2095301183070485279589016 |
| gluon_s1_s1 | -3.151088420630975731134374 | 0.209913619275028895066292 | glide reflection | 0.2095301183070485279589016 |
| gluon_s0_s0 | -3.151088420630975731134374 | 0.1043880582591816378331172 | glide reflection | 0.1043407203195195123159063 |
| nuc11_gen_grouped | -3.151088420630975731134374 | 0.5380646002988595108999592 | glide reflection | 0.5317766153655461885306471 |

## t=-q0

| word | det | x = abs(tr)/sqrt(abs(det)) | type | length |
|---|---|---|---|---|
| nuc9 | 2.557592746943598482591003 | 0.0 | elliptic | 0.0 (rotation 3.141592653589793238462643) |
| nuc11_interleaved | 3.151088420630975731134374 | 2.00272236386053329050782 | hyperbolic | 0.1043407203195195123159063 |
| gluon_s0_s1 | 3.151088420630975731134374 | 2.00272236386053329050782 | hyperbolic | 0.1043407203195195123159063 |
| gluon_s1_s0 | 3.151088420630975731134374 | 4.027268126371427698669651 | hyperbolic | 2.649587989469697311634308 |
| gluon_s1_s1 | 3.151088420630975731134374 | 4.027268126371427698669651 | hyperbolic | 2.649587989469697311634308 |
| gluon_s0_s0 | 3.151088420630975731134374 | 2.00272236386053329050782 | hyperbolic | 0.1043407203195195123159063 |
| nuc11_gen_grouped | 3.151088420630975731134374 | 26.78406822131797390571265 | hyperbolic | 6.572820737191481213029179 |

## Post-hoc observation (not pre-registered)

The three words that are parabolic at t = -1 (nuc11_interleaved = gluon_s0_s0, gluon_s0_s1) have length exactly ln q0 = 0.1043407203195195123159063 at both t: t=+q0 agrees to 1e-40, t=-q0 agrees to 1e-40. Exact reason: tr = t^5 (t - 1), det = -t^11.
