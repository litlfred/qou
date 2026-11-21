---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-029-71-eval-eval-name-predicate
section_title: "eval: eval <name> <predicate>"
section_number: 7.1
pages: 22-26
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:eval}
This is the most important command in Walnut and it stands for ``evaluate.'' This command takes two arguments. The first argument is a name for the evaluation. Name of the evaluation starts with a letter and could contain alphanumerics and underscore. The files generated as the result of the eval command, all share the name given in the first argument. The second argument is a predicate that we want to evaluate. Predicates are always placed between quotation marks. To see the definition for predicates see Section \ref{sec:predicates}. In this article we typeset predicates in math mode in \LaTeX. However, the reader should note that this typesetting is different from the one they see in the terminal. Let us see an example:
\begin{lstlisting}[style=cmd]
eval four "(*\textcolor{blue}{$a=4$}*)":
(@(*\textcolor{out}{$a=4$}*): 4 states - 3ms
total computation time: 3ms@)
\end{lstlisting}
This evaluates to an automaton with one binary input labeled $a$. This
is the automaton $(a):a=4$. To learn about the notation $(a):a=4$ see
Section \ref{sec:automata accepting predicates}. The automaton accepts
only if $a$ is the most-significant-digit-first binary representation
of $4$, i.e., if it belongs to $0^*100$. This automaton is drawn and
saved in the directory ``/Walnut/Result/'' in a file named four.gv as
shown in Figure \ref{fig:four}. The graph drawing software Graphviz is
required to open this file; see Section \ref{sec:installation}.

\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{four}
	\caption{Content of the file four.gv}
	\label{fig:four}
\end{figure}

How does Walnut know to use the most-significant-digit-first binary
system? Walnut defaults to $\MSD[2]$ which is how we show the
most-significant-digit-first binary system in Walnut; see Section
\ref{sec:number systems} to learn about this notation and to learn
about number systems in general. To explicitly mention $\MSD[2]$ type:
\begin{lstlisting}[style=cmd]
eval four "(*\textcolor{blue}{$\text{?msd\_2 } a=4$}*)";
\end{lstlisting}
Similarly,  for the least-significant-digit-first binary type:
\begin{lstlisting}[style=cmd]
eval lsd_four "(*\textcolor{blue}{$\text{?lsd\_2 } a=4$}*)";
\end{lstlisting}
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{lsd_four}
	\caption{lsd\_four.gv}
	\label{fig:four in lsd 2}
\end{figure}

Here is another example, this time in $\LSD[3]$:
\begin{lstlisting}[style=cmd]
eval ternary_example "(*\textcolor{blue}{$\text{?lsd\_3 } a<5$}*)";
\end{lstlisting}
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{ternary_example}
	\caption{ternary\_example.gv}
	\label{fig:ternary example}
\end{figure}

This automaton accepts exactly those words representing the numbers
$0$,$1$,$2$,$3$,and $4$ in the least-significant-digit ternary base,
i.e., $0^*$,$10^*$,$20^*$,$010^*$,$110^*$ respectively. Note the
trailing zeros in the representations as opposed to the leading zeros
in a most-significant-digit-first ($\MSD$) number system. Also note
that this automaton accepts the empty word. This is because in the
definition of number systems we agreed that the empty word represents
$0$.

Let us see an example of an automaton with $2$ inputs:
\begin{lstlisting}[style=cmd]
eval two_inputs "(*\textcolor{blue}{$b=a+1$}*)";
\end{lstlisting}
This constructs the automaton $(a,b):b=a+1$ in which the first input corresponds to $a$, and the second input corresponds to $b$. Recall from Section \ref{sec:automata accepting predicates} that Walnut uses lexicographic ordering on the name of variables when constructing automata. So, for example, even though the first variable that appears in $b=a+1$ is $b$, it corresponds to the second input in the automaton.
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{two_inputs}
	\caption{two\_inputs.gv}
	\label{fig:two inputs}
\end{figure}

Walnut generates two other files as the outcomes of the eval command
which can also be found in the directory \linebreak
``/Walnut/Result/''. For the evaluation two\_inputs, these two files
are named two\_inputs\_log.txt and two\_inputs.txt and they are both
text files.

The file two\_inputs\_log.txt contains the details of the evaluation
including the intermediate steps and the time each of those steps took
to complete. In our example, there are not many intermediate steps
involved:

\begin{figure}[H]
\begin{CenteredBox}
\begin{lstlisting}[style=cmd]
(*$b=2$*): 3 states - 0ms
total computation time: 0ms
\end{lstlisting}
\end{CenteredBox}
\captionof{lstlisting}{two\_inputs\_log.txt}
\end{figure}

In addition to two\_inputs\_log.txt , another file with the name two\_inputs\_detailed\_log.txt will be created if the command ends in two colons instead of a colon or a semicolon.

The file two\_inputs.txt contains the definition of the automaton in Figure \ref{fig:two inputs}:
\begin{figure}[H]
\begin{CenteredBox}
\begin{lstlisting}[style=file]
msd_2 msd_2
0 0
0 0 -> 0
0 1 -> 1
1 1 -> 0
1 1
1 0 -> 1
\end{lstlisting}
\end{CenteredBox}
\captionof{lstlisting}{two\_inputs.txt}
\label{file:two inputs}
\end{figure}

Line $1$ indicates that the first and the second inputs of the
automaton are both in $\MSD[2]$. The two states $0$ and $1$ in Figure
\ref{fig:two inputs} are declared in Lines $2$ and $6$. The first zero
in Line $2$ refers to the state $0$ and the second zero refers to its
output. Likewise, the first one in Line $6$ refers to the state $1$ and
the second one refers to its output. Note that the automaton for
evaluation two\_inputs is not an automaton with output, however all
automata are stored as automata with outputs in Walnut; see Section
\ref{sec:words and automata}. For an ordinary automaton, states with
non-zero outputs are interpreted as final states, and states with zero
outputs are interpreted as non-final states. So here state $0$ is
non-final, whereas state $1$ is final. Transitions for states $0$ and
$1$ are declared in Lines $3$-$5$ and $7$ respectively. For example,
state $0$ on $(0,0)$ transitions to itself, and on $(0,1)$ transitions
to state $1$. Transitions not depicted are transitions to the dead
state. For example, state $1$ transitions to the dead state on every
tuple except $(1,0)$. To learn more about definition of an automaton in
text files and how to manually define automata in text files see
Section \ref{sec:define automata in text files}.

In Section \ref{sec:automatic words}, we talked about the Thue-Morse
word. The Thue-Morse word's corresponding automaton with output,
depicted in Figure \ref{fig:thue}, is defined in directory
``/Walnut/Word Automata Library/'' in a file named T.txt. We can refer
to the Thue-Morse word in predicates by typing $T$. See Section
\ref{sec:define new automatic words} on how to define new automatic
words in Walnut.

We talked about square subwords in the Thue-Morse word. The following predicate is satisfied by $(i,n)$ if \linebreak$T[i..i+n-1]=T[i+n..i+2n-1]$, i.e., if there exists a square subword of length $2n$ starting at position $i$. 
\begin{lstlisting}[style=cmd]
eval squares_in_thue_morse_word "(*\textcolor{blue}{$n>0 \mathbin{\&}(\text{A}k\text{ } k< n\mathbin{\text{=>}}T[i+k]=T[i+n+k])$}*)";
\end{lstlisting}
The order of a square is half its length. Now if we want to find all natural numbers $n$ for which there exists a square of order $n$ in the Thue-Morse word, we simply use the existential quantifier E:
\begin{lstlisting}[style=cmd]
eval order_of_squares_in_thue_morse_word "(*\textcolor{blue}{$\text{E}i\text{ }n>0 \mathbin{\&}(\text{A}k\text{ } k< n\mathbin{\text{=>}}T[i+k]=T[i+n+k])$}*)";
\end{lstlisting}
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{order_of_squares_in_thue_morse_word}
	\caption{order\_of\_squares\_in\_thue\_morse\_word.gv}
	\label{fig:order of squares in thue morse word}
\end{figure}
Based on this automaton, the natural number $n$ with $\MSD[2]$ representation of the form $0^*(1|11)0^*$ is an order of a square in the Thue-Morse word. In other words, the set of orders in the Thue-Morse word is $$\big\{n:\text{there exists } k \geq 0\text{ such that }n=2^k \text{ or } n=2^{k+1}+2^{k}\big\}$$

Overlaps are the words of the form $axaxa$ where $a$ is a symbol and
$x$ is any word, e.g., the word ``alfalfa'' in English is an overlap. It is
a known that the Thue-Morse word avoids overlaps. How do we make sure,
using Walnut, that the Thue-Morse word does not have any overlaps? The
result of the following predicate must be the true automaton; see
Section \ref{sec:true and false}, if the Thue-Morse does not have any
overlaps:
\begin{lstlisting}[style=cmd]
eval thue_morse_does_not_have_overlaps "(*\textcolor{blue}{$\sim(\text{E}i,n\text{ }n>0 \mathbin{\&}(\text{A}k\text{ } k\mathbin{\text{<=}} n\mathbin{\text{=>}}T[i+k]=T[i+n+k]))$}*)":
(@(*\textcolor{out}{$n>0$}*): 2 states - 1ms
  (*\textcolor{out}{$k<=n$}*): 2 states - 1ms
    (*\textcolor{out}{$T[(i+k)]=T[((i+n)+k)]$}*): 12 states - 6ms
      (*\textcolor{out}{$(k\mathbin{\text{<=}}n\mathbin{\text{=>}}T[(i+k)]=T[((i+n)+k)])$}*): 25 states - 1ms
        (*\textcolor{out}{$(A k (k\mathbin{\text{<=}}n\mathbin{\text{=>}}T[(i+k)]=T[((i+n)+k)]))$}*): 1 states - 27ms
          (*\textcolor{out}{$(n>0\mathbin{\&}(A k (k\mathbin{\text{<=}}n\mathbin{\text{=>}}T[(i+k)]=T[((i+n)+k)])))$}*): 1 states - 0ms
            (*\textcolor{out}{$(E i , n (n>0\mathbin{\&}(A k (k\mathbin{\text{<=}}n\mathbin{\text{=>}}T[(i+k)]=T[((i+n)+k)]))))$}*): 1 states - 1ms
              (*\textcolor{out}{$\sim(E i , n (n>0\mathbin{\&}(A k (k\mathbin{\text{<=}}n\mathbin{\text{=>}}T[(i+k)]=T[((i+n)+k)]))))$}*): 1 states - 0ms
total computation time: 38ms@)
\end{lstlisting}
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{thue_morse_does_not_have_overlaps}
	\caption{thue\_morse\_does\_not\_have\_overlaps.gv}
	\label{fig:thue_morse_does_not_have_overlaps}
\end{figure}
The automaton in Figure \ref{fig:thue_morse_does_not_have_overlaps} is the true automaton. For more information see Section \ref{sec:true and false}.

Note that if a predicate is not valid Walnut returns an error:
\begin{lstlisting}[style=cmd]
eval invalid "(*\textcolor{blue}{$x+y+z$}*)";
\end{lstlisting}
\vspace*{-\baselineskip}
\begin{lstlisting}[style=err]
the final result of the evaluation is not of type automaton
	: eval invalid "(*$x+y+z$*)";
\end{lstlisting}

To understand why this is not a valid predicate see Section \ref{sec:arithmetic expressions}. In the following examples note how Walnut points to the locations of the errors in the predicates. By saying "char at $n$", Walnut tries to convey that there is something wrong going on at the vicinity of the $n$'th character in the predicate.
\begin{lstlisting}[style=cmd]
eval invalid2 "(*\textcolor{blue}{$(x+y+z=0$}*)";
\end{lstlisting}
\vspace*{-\baselineskip}
\begin{lstlisting}[style=err]
unbalanced parenthesis
	: char at 0
	: eval invalid2 "(*$(x+y+z=0$*)";
\end{lstlisting}
\begin{lstlisting}[style=cmd]
eval invalid3 "(*\textcolor{blue}{$({\sim x})=0$}*)";
\end{lstlisting}
\vspace*{-\baselineskip}
\begin{lstlisting}[style=err]
operator (*$\sim$*) cannot be applied to the operand (*$x$*) of type variable
: char at 1
: eval invalid3 "(*$({\sim x})=0$*)";
\end{lstlisting}
\begin{lstlisting}[style=cmd]
eval invalid4 "(*\textcolor{blue}{$T[i+j]=i-1$}*)";
\end{lstlisting}
\vspace*{-\baselineskip}
\begin{lstlisting}[style=err]
operator = cannot be applied to operands (*$T[(i+j)]$*) and (*$(i-1)$*) of types word and arithmetic respectively
	: char at 6
	: eval invalid4 "(*$T[i+j]=i-1$*)";
\end{lstlisting}
\begin{lstlisting}[style=cmd]
eval invalid5 "(*\textcolor{blue}{$T[2]=1$}*)";
\end{lstlisting}
\vspace*{-\baselineskip}
\begin{lstlisting}[style=err]
operator = cannot be applied to operands (*$T[2]$*) and (*$1$*) of types word and number literal respectively
	: char at 4
	: eval invalid5 "(*$T[2]=1$*)";
\end{lstlisting}
The last example can be fixed as follows:
\begin{lstlisting}[style=cmd]
eval fixed5 "(*\textcolor{blue}{$T[2]=@1$}*)";
\end{lstlisting}
To understand why see Section \ref{sec:relative expressions}.

The last thing to note about the eval command is that Walnut overrides the files generated by an evaluation if the name of the evaluation is used in a new evaluation.
