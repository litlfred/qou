---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-025-16-complexity-and-firewalls
section_title: "Complexity and Firewalls"
section_number: 16
pages: 55-59
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
text_source: latex
latex_prose_ratio: 0.627
latex_coverage_ratio: 1.0
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
Let me
come now to the subject of firewalls. A firewall is supposed to be an extremely intense high energy shock wave propagating on or just behind the horizon. 
There are two paradoxes, both of which were claimed to be solved by firewalls. One is connected with entanglement and the other with ``typicality." The paradox of multiple entanglements is solved by the ER=EPR principle and I will not discuss it further. The ``Typical State Paradox" (D. Marolf and J. Polchinski, \url{https://arxiv.org/pdf/1307.4706.pdf}) 
is the one whose resolution has to do with complexity 
\url{https://arxiv.org/pdf/1507.02287.pdf}.


The typical state paradox can be easily explained in the case of the two-sided black hole. Imagine Bob on the right side and Alice on the left. Bob would like to jump into his black hole but without getting burned up at the horizon. The problem is that he has no idea what Alice might have done at her end. If one considers all the possible things she could have done  one may conclude that the situation is very dangerous. After all, she had all negative time, deep into the remote past, during which she might have perturbed her black hole. For example she might have dropped in one or more thermal photons deep in the exponential past. Almost anything she did in the remote past would have created  very intense shock waves or firewalls. So averaging over all possibilities, Bob should conclude that there is, with overwhelming likelihood, a firewall/shockwave at his horizon.

That's the typical state argument. Before discussing its relation with complexity I want to compare it to a  similar cosmological argument. Consider Charlie whose world line arrives at spacetime point $C$ in figure \ref{past}.

\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{past.pdf}
\caption{}
\label{past}
\end{center}
\end{figure}

He has a pretty good idea of what's in his past light-cone but in principle, he cannot know what is in the shaded region outside his causal past. Charlie would like to know what will happen to him in the next instant. So he averages over his ignorance, or to put it another way, he Haar-averages over all states that agree with his past experience. What he finds is very frightening. Almost all states consistent with Charlie's past contain a tremendous blast of super-high energy particles just outside his current past light-cone as in figure \ref{blast}.

\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{blast.pdf}
\caption{}
\label{blast}
\end{center}
\end{figure}

\bn
So with virtual certainty he concludes that he will be burned to a crisp in the next nanosecond.

It's obvious what is wrong with this conclusion. Charlie needs a better cosmological theory of how his past is embedded in a larger spacetime. I won't go further into the details of cosmology here, but any reasonable theory of how Charlie got to his current location at $C$, the state of the world at that time is very exceptional---very un-Haar-typical.

The same thing is wrong with the the typical state theory of firewalls. I will explain why it is very likely that a Haar-random state of a condensed black-hole-like object \it does \rm have a firewall. But that ignores the question of how the black hole got there. We will see that any reasonable process of formation  of a black hole---stellar collapse is an example--- will give rise to a very atypical state.


\bn

Extremely energetic shock waves are certainly possible. Alice can create one on Bob's side by throwing in a thermal photon long in the past, at $t=t_w.$ To follow the complexity as a function of Bob's time we
return to the master formula \ref{master-formula}, this time   holding $\t_L$ fixed. We will  consider the complexity as a function of $\tau_R.$ In doing so we will see an surprising feature of  formula \ref{master-formula} . 
For $\tau_L = 0$,
\be 
V= const \log{  \{
\cosh\frac{\tau_R}{2} + e^{(|\tau_w|-\tau_*) - \frac{1}{•2}\tau_R}
\}
}
\label{tL=0}
\ee
Assume that $|\tau_w|>> \tau_*$ in which case the shock wave will be super-Planckian (recall the the energy of the shock wave grows exponentially with $|t_w|$). For $\tau_R$ not too large the second term dominates so that even at positive time the complexity \it decreases \rm as a function of $\tau_R.$ This is somewhat strange because  decreasing complexity violates the second law of complexity. Of course this is not really a law but a statistical tendency, but it may seem surprising that the mere act of throwing in a thermal quantum on the left can lead to decreasing complexity on the right. That seems too easy; violating the second law should be harder than that.

The point is that it \it is \rm hard---very hard. To create the shock wave we either had to start with the white hole in the remote past---an extremely fine tuned thing to do---or we have to apply a precursor which effectively means running the system backward for a long period of time. This is also very hard and unstable.
Evidently creating a firewall requires reversing the arrow of time and that is bound to be extraordinarily difficult. 





The full history of the eternal black hole  generally has decreasing complexity in the white hole region. That is obvious from figure \ref{Foliated-BTZ2}, but the decrease is in the negative time region. In the shock wave case the decreasing  complexity  extends deep into the positive time region on Bob's side. 
It does eventually turn around when the two terms in \ref{tL=0} cross over at, $$t_R = |t_w| -t_*.$$  At that time the complexity begins to increase, but it only achieves its normal rate of increase far in the future  when $t = |t_w|.$

This behavior  is quite striking as can be seen from figure \ref{firewall}.
\bn
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{firewall.pdf}
\caption{An initially super-Planckian shockwave will eventually separate from the Planckian region and fall into the singularity. This occurs just at the Eddington-Finkelstein time when the complexity stops decreasing.}
\label{firewall}
\end{center}
\end{figure}

The grey region is within a Planck distance of the horizon as seen by an infalling observer. Any shockwave in that region is superplanckian. The red line is a shockwave which crosses out of the Planckian region and then falls into the singularity. The green lines are constant Edington-Finkelstein time slices. What we see is that the complexity decreases until the shockwave moves out of the Planckian region. As the shock wave approaches the singularity the complexity resumes its normal rate of growth, Zhao, \url{https://arxiv.org/pdf/1702.03957.pdf}. 




The decrease of complexity is closely correlated with the location of the shock wave. One can see from figure \ref{shock-wave} that the more negative $t_w$ is, the closer to the right-side future horizon the shock wave will be. For very large $|\tau_w|$ the shock wave stays within a Planck distance of the horizon for a very long time before separating and falling into the singularity. In fact if we use Eddington-Finkelstein infalling coordinates for the right-side black hole, we find that the complexity turns around and starts to increase precisely when the shock wave separates from Planckian distance from the horizon.



Because the firewall is associated with decreasing complexity one might expect it to be unstable.  Let's suppose that $t_w$ is very far in the remote past and that Bob wants to jump into the black hole without being destroyed by the shock wave. All he has to do is throw in a single thermal photon. The result is shown in figure \ref{kick}.

\subsection{Firewalls are Fragile}\label{Sec: fragile FW}

\begin{figure}[H]
\begin{center}
\includegraphics[scale=.4]{kick.pdf}
\caption{An intially super-Planckian shockwave will be ``kicked" into the singularity by a single thermal quantum. The green region is the  Plankian region.}
\label{kick}
\end{center}
\end{figure}

The photon and the shock wave will undergo a high energy collision. On can think about the collision from the point of view of a frame in which the photon is high energy and the shock wave is low energy. In other words we can exchange the role of the photon and the shock wave. In that frame the infalling photon causes a Dray-'t Hooft shift of the original shock wave, kicking it out of the Planckian region and pushing it deeper into the black hole. The calculation is easy and one finds that no matter how high the energy of the original shock wave, it will fall into the singularity approximately a scrambling time after the photon is thrown in.
The lesson is that shock waves or firewalls are very fragile and can be destroyed by a single thermal photon. If Bob throws in the photon and waits a scrambling time he can be sure that the horizon will be transparent.

Lecture III is all about the counter-intuitive power of a single qubit---in this case a thermal photon---to accomplish what seem like impossible tasks. One of those tasks is destroying a firewall of tremendous energy\footnote{The energy of a shock wave grows exponentially with $|t_w|$. For reasons explained in Section \ref{expTbreakdown} \  the classical shock wave analysis holds up to exponential time $\exp S.$  A shock wave produced at that time has doubly exponential energy $\exp \exp S$ in the frame of an infalling observer.}
\bn

To get some sense for the orders of magnitude involved consider a solar mass black hole that has a super-Planckian shock wave behind the horizon. A single radio frequency photon with a wave length of a kilometer will destroy the firewall in a scrambling time which happens to be about a millisecond. A CMB microwave photon will destroy it even faster.

\bn




To summarize, firewalls are both very difficult to create and very fragile. To create one Alice must apply a precursor that effectively runs her black hole backward in time in order to create the shock wave. And to get rid of a firewall Bob only needs to drop in a thermal photon.




\subsection{What Happens After Exponential Time?}




Let's suppose that it is true that once complexity equilibrium is established, there is a high probability for a firewall. How stable is that firewall? The naive answer is that equilibrium is  stable and not likely to be significantly disturbed by butterflies. That is true for ordinary thermal equilibrium but complexity equilibrium is different.




Recall from Lecture I that the transition from growing complexity to equilibrium occurs abruptly when the complexity reaches its maximum $e^S$. Now suppose a thermal photon is  thrown in. It will increase the entropy by only one unit which seems negligible. But  the maximum complexity changes from  $e^S$ to $e^{S+\log{2}} = 2\times e^S.$
This means the black hole suddenly finds itself exponentially far from maximal complexity, with plenty of room for complexity to increase for another exponential time. 



At exponentially large time, $t=\exp{K},$ the system reaches complexity-equilibrium and the complexity suddenly\footnote{At the end of the first lecture I explained why the transition is sudden.} stops growing. Something non-classical happens and the question is how does this affect an observer who falls through the (right) horizon? First let's ask the question for evolution of the exact TFD state.

The answer in this case is  that nothing special happens. The reason is that $|TFD\ra$ has a special symmetry, sometimes called time-translation symmetry.  But its not really time-translation; it's  boost symmetry in which $t_R$ and $t_L$ shift in opposite directions,
\bea
t_R &\to& t_R +c \cr \cr
t_L   &\to& t_L -c
\label{boost}
\eea
The transformation is generated by the difference of right and left Hamiltonians,
\be 
\rm Boost \ Generator \it \ = H_R-H_L
\ee

Let's call the operator that emits Bob from the boundary $B(t_R)$ and the time that he is emitted, $t_R = T$. The state after Bob has entered the geometry is
\be 
B(T) \ |TFD\ra.
\ee
The argument is  that a boost can transform this state  to
\be 
B(0) \ |TFD\ra,
\ee
so  that even if $T$ is exponentially large, it has no effect.

The thermofield double state is  very fine-tuned,  but we may ask what happens if we break the boost symmetry by a tiny amount. Again the answer is not much  if  $T$ is not very large, but if it is large all bets are off. 

To break the symmetry let's suppose that Alice, on the left side, perturbs the system at $t_L=0$ with a thermal photon. She does this  by applying the operator $A(0)$. As before Bob jumps in at $t_R=T$. The state of the system becomes,
\be 
A(0)B(T) \ |TFD\ra
\ee
We can again transform Bob to $t_R=0$ but now Alice's perturbation is transformed to $t_L = T.$
\be 
A(0)B(T) \ |TFD\ra  \to  A(T)B(0) \ |TFD\ra
\label{ABTFD}
\ee
This is illustrated in figure \ref{boost1}.

 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.2]{boost.pdf}
\caption{}
\label{boost1}
\end{center}
\end{figure}

We can write the rhs of  \ref{ABTFD} as
\be 
 A(T)B(0)  \ |TFD\ra = e^{-iH_LT}A(0)e^{iHT}B(0 ) \ |TFD\ra
 \label{ABTFD1}
\ee
This time we cannot eliminate Alice's perturbation, but we might think it is not important. It looks safely out of the way in the upper left corner of the diagram. To see that this argument is flawed we go to an extremely late  quantum recurrence time. The point of the quantum recurrence time is that $e^{-iHT}$ can be arbitrarily close to the unit operator $I$. In that case \ref{ABTFD1} becomes,
\be 
 A(T)B(0) \ |TFD\ra =  A(0)B(0) \ |TFD\ra
 \label{ABTFD2}
\ee
In fact if we make $T$ less than the recurrence time by twice the scrambling time the state becomes
\be 
 A(T)B(0) \ |TFD\ra =  A(-2t_*)B(0) \ |TFD\ra.
 \label{ABTFD3}
\ee

The state \ref{ABTFD3} is not benign; it is extremely dangerous to Bob. It contains a very high energy shock wave created by $A(-2t_*)$ which Bob will experience as a firewall.
This is an existence proof that if the boost symmetry is slightly broken then Bob's classical expectations of a transparent horizon will be wrong if he jumps in late enough at just the wrong time. 

 

I don't know what happens at the earlier singly exponential time when complexity stops increasing. I'd like to show that firewalls have a high probability of occurrence but I can't. But I have also been unable to show that firewalls don't occur. The Marolf-Polchinski generic state argument suggests that they do and I will accept that. 


\subsection{The Fragility of Complexity Equilibrium}


Let's  take the default position: If there is no reason to believe that  firewalls don't occur when the complexity stops increasing, then they probably do occur.
 How stable would such a firewall be? The naive answer is that equilibrium is  stable and not likely to be significantly disturbed by butterflies. 
 That is true for ordinary thermal equilibrium, say of a gas of $N$ classical molecules. 
 
 Thermal equilibrium is a state of maximum entropy in which the entropy is proportional to the number of molecules,
 \be 
 S_{max}\sim N.
 \ee
Now lets perturb the state by adding a single molecule. The result will be that the maximum entropy will be increased by one bit,
\be 
S_{max} \to N+1.
\ee

Although initially out of equilibrium, the new molecule will  come to equilibrium with the new entropy being $\sim N+1.$ This will typically take a very short time.

Let's compare this with what happens if we add a single qubit to a system of $K$ qubits in complexity equilibrium. The maximum complexity of the original $K$ qubit system is $2^K.$ Adding a qubit brings the maximum complexity to $2^{(K+1)}= 2\times 2^K$. This means that the new state is far out of complexity equilibrium; the complexity can increase for an additional amount $\sim 2^K.$
  
Now let's return to the black hole in complexity equilibrium at maximal complexity. If we drop in a single thermal photon the entropy increases by one bit, but the maximal complexity doubles.
The system has been kicked far out of complexity equilibrium by the addition of a thermal photon.
To return to equilibrium a minimum of $2^K$ gates must act, and this will take an exponential time. By dropping in the thermal photon we buy an additional exponential time during which the complexity increases. Complexity equilibrium is evidently very fragile. 


There is another way to think about this. If indeed a black hole in complexity equilibrium has a firewall at its horizon, throwing in a thermal photon will   have the same effect as in section \ref{Sec: fragile FW}. The photon will kick the shock wave  and push it into the singularity. The horizon will be clear and the wormhole will be free to grow again for another exponential time.

\bn
