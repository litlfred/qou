---
doc_id: 1-s20-s002212362200012x-main
doc_title: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-007-22-stochastic-localization
section_title: "Stochastic localization"
section_number: 2.2
pages: 9-12
source_pdf: 1-s2.0-S002212362200012X-main.pdf
source_sha256: 6fc7d28c8d40bf42
toc_source: outline
doc_brief: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube — V Article history: Received 17 December 2020 Accepted 13 January 2022 Available online"
---
We construct a stochastic process driven by a Brownian motion, which we refer to as 
stochastic localization. A somewhat similar process was originally used in [6] to establish 
concentration properties for log-concave measures on Rn. Here we use a discrete version, 
similar to the construction which appears in [7,8]. In this section we occasionally allow 
ourselves to omit some of the details of the proofs, and the reader is referred to [7] for 
more rigorous derivations.
The high-level plan is to construct a stochastic evolution of measures (νt)t≥0 on Cn
such that ν0 = ν and such that νt converges to a Dirac measure supported on a random 
point x ∈Cn. This process will be a martingale in the sense that M ϕ
t
:=

Cn ϕdνt is 
a martingale for every test function ϕ : Cn →R, which will allow us to decompose 
the variance Varν[ϕ] into two terms, one involving the quadratic variation of M ϕ
t and 
the other of the form EVarνt[ϕ]. The main step in our proof will be to show that the 
quadratic variation d[M ϕ]t can be bounded by an expression involving the modulo of 
log-concavity of ν.
Let Bt be a standard Brownian motion on Rn adapted to a ﬁltration Ft. Consider 
the system of equations,
F0(x) = 1,
dFt(x) = Ft(x)⟨x −at, dBt⟩,
∀x ∈Cn,
(10)
where at :=

xFt(x)dν(x). Finally, deﬁne the measures νt by the equation
dνt
dν (x) = Ft(x),
∀x ∈Cn.
Clearly, by deﬁnition we have ν0 = ν. We will see below that the process νt ends up 
with a Dirac measure whose support is ν-distributed. Let us ﬁrst summarize some useful 
properties of this process.
Proposition 10. The process deﬁned above satisﬁes the following properties.
1. Almost surely, for all t, νt is a probability measure.
2. For all A ⊂Cn, the process νt(A) is a martingale.
3. The process at almost surely converges to a point in Cn, and a∞:= limt→∞at is 
distributed according to the law ν. Moreover, the measure νt almost-surely weakly 
converges to a Dirac measure at a∞.
10
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
Proof. We have
dνt(Cn) = d

Cn
Ft(x)ν(x) =

Cn
(x −at)dνt(x)dBt = 0,
which proves the ﬁrst part. The second part is evident from the deﬁnition. For the third 
part, a calculation gives,
dat = d

Cn
xνt(x)
=
⎛
⎝

Cn
x ⊗(x −at)νt(dx)
⎞
⎠dBt
=
⎛
⎝

Rd
(x −at)⊗2νt(dx)
⎞
⎠dBt
= Cov(νt)dBt.
(11)
Therefore, at is a martingale, and
d[⟨at, ei⟩]t =

j∈[n]
Cov(νt)2
i,jdt ≥Cov(νt)2
i,idt = (1 −⟨at, ei⟩2)2dt,
(12)
implying that ⟨at, ei⟩converges to {±1} almost surely and that νt converges weakly to 
δa∞, which also implies that
lim
t→∞at ∈A ⇔lim
t→∞νt(A) = 1,
for all A ⊂Cn. Since νt(A) is a martingale, we have that
P

lim
t→∞at ∈A

= lim
t→∞Eνt(A) = ν(A),
implying the third part.

Next, we have by Itô’s formula, for all x ∈Cn,
d log Ft(x) = dFt(x)
Ft(x) −d[F(x)]t
2Ft(x)2
= ⟨x −at, dBt⟩−1
2|x −at|2dt
= ⟨x, dBt + atdt⟩+ dZt
(13)
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
11
where Zt is an Itô process that does not depend on x (here we used the fact that |x|2 is 
constant on Cn). Therefore,
log Ft(x) = ⟨x, wt⟩+ ct
where ct is some Itô process and wt = Bt +

 t
0 asds. The above display and the fact that 
νt is a probability measure, implies that
νt = τwtν,
(14)
and therefore also
at =

Cn
xdνt(x) =

Cn
xdτwtν(x) = aν(wt).
The process wt thus satisﬁes the equation
w0 = 0,
dwt = dBt + aν(wt)dt.
(15)
The above equation gives an alternative construction for the process deﬁned in (10). Due 
to the Markov property of the measure-valued process νt, the above discussion leads to 
the following result.
Proposition 11. Given a measure ν and a vector v ∈Rn, consider the process deﬁned by 
the equation
u0 = v,
dut = dBt + aν(ut)dt.
Then X = limt→∞aν(ut) exists and is a point in Cn almost surely, and has the law τvν.
Proof. Consider the measure ˜ν = τvν and let wt be the process constructed as above 
with ν replaced by ˜ν in equation (10). Observe that by deﬁnition
a˜ν(x) = aν(x + v),
∀x ∈Rn.
In light of (15) and by the uniqueness of the solution to the above SDE, we have that 
wt + v = ut almost surely, for all t. The result now follows from part 3 of Proposition 10
and the fact that
at = a˜ν(wt) = aν(ut).

12
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
