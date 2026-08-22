---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-022-142-lyapunov-and-rindler
section_title: "Lyapunov and Rindler"
section_number: 14.2
pages: 49-51
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
Let’s come back to the relation between circuit clock time and Rindler time. You may think
that the arguments were not very compelling but equations 14.49 through 14.54 provide
a quantitative basis for the identiﬁcation. The exponential growth in 14.54 is expected
and should be compared with the OTOC theory of scrambling, especially as applied to
black holes. There it is well known from the work of Kitaev and Maldacena, Shenker, and
Stanford, that in black hole physics size grows according to,
s(t)≈e
2π
β t (14.57)
The quantity 2π/β is called the quantum Lyapunov exponent and it is universal for large
black holes as long as the Schwarzschild radius is much larger than the string scale.
Comparing 14.57 with 14.54 we see that agreement indeed requires,
τ = 2π
β t. (14.58)
In other words circuit time is Rindler time.
Back to Size and Complexity
Let us now consider the total number of un-cancelled gates in ﬁgure 23. This number is
the complexity of the precursor at time τ.
#uncanceled gates =C(τ).
The number of such gates on the right side at any discrete time n is the sum of the sizes
for all times less than or equal to n. In terms of the continuous time we can write,
C(τ) =
∫ τ
0
s(τ′)dτ′ (14.59)
or using 14.51,
C(τ) =K log(1 +eτ−τ∗). (14.60)
48
For large K the size and complexity of the precursor are negligibly small (compared
to K) until the scrambling time at which they quickly grow to K. After that the size is
constant and the complexity grows linearly. The delay in the growth of complexity by τ∗
is called the switchback eﬀect (Stanford and Susskind, https://arxiv.org/pdf/1406.
2678.pdf) and is an important diagnostic that we will use later. The time-dependence of
size and complexity are shown in ﬁgures 25 and 26.
Figure 25: size as a function of time
Figure 26: as a function of time
49
Now let us turn to precursors in black hole physics. We will see some remarkable
correspondences between the geometry of black hole interiors and the equations that we
have derived from the analysis of circuits.
