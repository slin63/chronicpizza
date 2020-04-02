---
title: "🔌 • consensus: a beautiful problem in distributed systems"
date: 2020-04-02T12:33:04-05:00
draft: true
---

{{% imagelink %}}/images/consensus/1.jpg{{% /imagelink %}}

## Consensus First Explained Rigorously, then Absurdly

#### Rigorously

You have *N* processes in a network. These processes communicate with one another by sending messages. Messages are packets of information. Any of those processes may fail at any time, becoming unresponsive to incoming messages and not sending out any messages themselves.

Any responsive, non-failed process is called a *correct* process. The problem of consensus is described in the following three requirements:

- *Agreement*: You must try and get all correct processes to agree on a single value, as proposed by any single process in the network.
  - *e.g.* a collection of banking computers deciding whether or not you're the true owner of your bank balance.
- *Validity:* All processes that return a value must have that value be a function of some input value from some other correct process, and not some arbitrary random or predefined value.
  - *e.g.* none of those banking computers can be programmed to just automatically respond with "actually, it's the person who wrote my software's balance." That, or the computer picks a name from a random pile of customers.
- *Termination*: All correct processes must eventually return a value.
  - e.g. all banking computers wait for all other computers to decide whose balance it is rather than immediately accepting the first, potentially incorrect, name.

Consensus exists everywhere around us. In all the websites that we use, in our home devices, our laptops and phones, even in our most basic human interactions.

#### Absurdly

People implement and exercise extremely convoluted solutions to far more rigorous forms of the consensus problem every day. Consider the following example.

- A group of friends must decide where to eat in New York, a city with roughly 26,618 eateries.

  Mike wants falafel cart. But Samantha hates falafel because of an irrational hatred for chickpeas. She proposes dollar pizza. James hates dollar pizza, because it gave him diarrhea last week, and the week before. Mike hears everyone's complaints and suggests Chinese food, which has neither chickpeas or pizza in it. David catches up to the group, after lagging behind while petting a dog, and proposes dollar pizza. Everyone explains to David why they can't do that.

  Suddenly, a giant meteor strikes the Earth. Nobody eats anywhere.

  12 years later, having survived the apocalypse, all our friends, except for Mike (RIP), who is succeeded by his 11 year old son, Muz∆¥løek, born of a world rapt in horror and uncertainty, rejoin and decide on a place to eat: the pile of burnt out cars on Parkside & Bedford in Brooklyn. They're going to have stone soup.

This is a nightmare.

Not because of the post-apocalyptic nature of this scenario. But, also not because they're going to the pile of burnt out cars on Parkside & Bedford to have stone soup, which is really the worst thing on the menu there.

It's a nightmare because out of the *N* processes, any single one can propose a value. But now these processes also have the ability to *veto* and remove values from the pool of choices. Also, there are arbitrary *pools of choices*, as opposed to the binary consensus problem we described earlier. Not to mention that these processes can lag behind and re-propose previously vetoed values, wasting network time. Then, without warning, we see that the system is one that can spontaneously fail.

Finally, despite all the setbacks and an incredible amount of network downtime, all *correct* processes rejoin and decide on a value. Also, in a turn of events completely irrelevant to our consensus problem, the *Mike* process managed to spawn a child process, Muz∆¥løek, who is allowed to participate in the network.

This is consensus.

So now that you have a feel for what the consensus problem is and how hairy it can become, let's talk about why it's so important.

## Consensus is Fundamental

Consensus serves as the basis for countless problems inside distributed systems. I'll list a few here.

- *Reliable Multicast*: Guarantee that all processes within a network receive the same update in the same order.
- *Membership/Failure Detection*: Having processes maintain a local list of all other processes in a network, updating on membership changes like processes leaving or failing.
- *Leader Election*: Agreeing on a single leader process and notifying the entire network of the new leader.
- *Mutual Exclusion/Distributed Locking*: Allow only one process at a time to access a critical resource, such as a file.

Any protocol for solving the basic problem of consensus, by extension, can also be leveraged to solve all of the above problems. Isn't that amazing?

With so many great minds in the field of distributed computing, consensus must have so many great and proven solutions! Aren't you excited?

## Consensus is Impossible

Surprise! Formally proven in *[Impossibility of Distributed Consensus with One Faulty Process](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf)*, consensus, although possible to achieve in *synchronous* systems, is impossible in an *asynchronous* system. The paper describes consensus as the following:

> an asynchronous system of [unreliable] processes . . . [trying] to agree on a binary value (0 or 1). Every protocol for this problem has the possibility of nontermination, even with only one faulty process.

To understand the asserted point here, it is important to distinguish some key differences between synchronous and asynchronous system models.

In a *synchronous system model*, there is a known upper bound on message delivery time between correct processes. If a process hasn't responded in that amount of time, it's failed. An example of a synchronous system might be a single supercomputer doing a lot of calculations.

In an *asynchronous system model*, messages can be delayed indefinitely, taking anywhere from 1ms to a year to never arriving to their destination. An example of an asynchronous system might be several computers, working together to do a larger calculation, assigning work and returning results over the network. 99% of real world over-network applications fall into this category.

Imagine a synchronous system trying to achieve consensus. If a process takes too long to respond to something, because of the upper bound on message delivery time, we know that that process is no longer *correct*, and that we don't have to wait on it for a response. Eventually all the *correct* nodes put in their votes, and consensus is achieved.

Now imagine an asynchronous system. If a process takes too long to respond to something, because *there is no* upper bound on message delivery time, how do we know that this process is guaranteed to be *no longer correct*? The answer: it's impossible. Failed processes and processes that are very slow to respond are indistinguishable in an asynchronous system.

Sure, you could implement a simple time-based failure detection protocol like I did with [Chord-ish](https://github.com/slin63/chord-failure-detector), but another problem arises. If we wrongly mark the slow process as failed and proceed with voting, we violate termination.

Termination requires that all correct processes must eventually return a value. Although our wrongly marked process is extremely slow to respond, it is still a correct process. Coming to a decision without considering that processes' output is a violation of termination.

This is just one of *many* ways that an asynchronous system can fail to come to true consensus.

But it's okay, don't worry.

## Most Protocols Are Good Enough

Although solving the formal problem of consensus in asynchronous systems is impossible, many protocols exist in the wild and are attached to names you might find [very familiar](https://en.wikipedia.org/wiki/Consensus_(computer_science)#Some_consensus_protocols). You might ask: "but isn't it literally impossible? How are there so many solutions"? Well, simply put, most solutions are adequate.

These adequate solutions provide consensus to distributed systems with high probability, but cannot guarantee it. They forgo the need for guaranteed consensus in exchange for probabilistic consensus, developing algorithms that minimize the risk of edge cases. Most practical solutions that provide probabilistic consensus satisfy the following requirements:

- *Safety*: servers never return an incorrect result, under non-[Byzantine failures](https://en.wikipedia.org/wiki/Byzantine_fault).
- *Availability*: servers always respond to a request as long as the majority of servers are operational and capable of communicating with each other and clients.
- *Timing Independent*: the protocol does not depend on timing to ensure consistency in the flow of data for each server.

## Conclusion

Consensus describes some arbitrary number of processes all agreeing on a single proposed value. It is a fundamental problem of distributed systems because solving the basic problem of consensus would also lead to the solving of more convoluted problems, such as reliable multicast, failure detection, and many others.

Consensus is possible in synchronous systems, but formally proven to be impossible in asynchronous systems, as a result of the indistinguishability of failed and slow processes. Despite this impossibility, many implemented solutions exist.  These solutions forgo the need for guaranteed consensus and provide consensus with high probability instead.

I hope that you now better understand the problem of consensus, its impossibility, and the requirements for a practical real-world solution.

In a future post, I'll begin talking about one of these real world solutions, [Raft](https://pdos.csail.mit.edu/6.824/papers/raft-extended.pdf), and how I utilized it as the consensus layer for [Chordish DeFiSh](https://github.com/slin63/chord-dfs).

{{% sources %}}

#### *sources*

1. Indranil Gupta (Indy), UIUC CS425, [Lecture A: The Consensus Problem](https://courses.engr.illinois.edu/cs425/fa2018/L14.C3.FA18.pdf)
1. Fischer et. al., [Impossibility of Distributed Consensus with One Faulty Process](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf)
2. Wikipedia, [Consensus](https://en.wikipedia.org/wiki/Consensus_(computer_science))

{{< pageend "🔌">}}
