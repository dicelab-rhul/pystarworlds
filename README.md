# PyStarWorlds

PyStarWorlds is currently a single container implementation of the [GOLEM](https://www.cs.rhul.ac.uk/home/kostas/pubs/debs09.pdf) framework implemented in Python. It rationalises various aspects of GOLEM and simplifies its agent model to support rapid prototyping of practical applications. The current system supports the deployment of multiple agents, that can observe and act in the environment in which they are situated. 

PyStarWorlds is currently in a prototype phase and can be thought of more as a library rather than as a standalone platform. 

### Iterations:

The history of this work is based on a series of iterations on the same topic, as follows:

- [GOLEM - Prolog/Java]() - this is the main framework of this work, developed in the PhD thesis of <a href="https://research.ou.nl/en/persons/stefano-bromuri-2">Stefano Bromuri</a>;
- [StarWorlds-Lite - Java](https://bitbucket.org/Beans20/starworlds-lite-fork/src/master/) - GOLEM on one container, developed by <a href="https://pure.royalholloway.ac.uk/portal/en/persons/benedict-wilkins(3b223c0c-c3f2-4526-bdcb-847cb733f6e3).html">Ben Wilkins</a>, for teaching purposes;
- [PyStarWorlds - Python (current)](https://github.com/dicelab-rhul/pystarworlds).

### Why shift to Python? 

- Great for prototyping, rapid development ecosystem with many useful libraries.
- Dynamic typing provides great advantages to developers using the platform. We have found a strongly typed language difficult to work with when building environments on top of StarLite, particularly when writing environment evolution rules - Java generics were not sufficient!
- The defacto language for machine learning research, part of our goal is to make it easy to develop agents with learning capabilities.
- Potential for future extension - a C/C++ backend means that the system has great potential for an efficient implementation, concurrency etc. 

# Environment

The enviroment uses two key abstractions _ambient_ and _physics_ explained below.

## Ambient

The (current) state of the environment which evolves in time according to the rules of the environment (physics). The implementation of the ambient is specific to the domain and is therefore left to the developer to define. 

## Physics

The physics is a collection of rules that govern the evolution of the environment. Events/actions are processed according to these rules. Notifications enable agent perception via a publish and subscribe mechanism. This mechanism is tied to the agents sensors, events that originate from environmental processes or other agents are received by any agent that subcribe to them.

## Containers * 

The GOLEM framework introduced containers as a mechanism for distributing agent environments, PyStarWorlds currently implements a single container. 

## Concurrency * 

The environment runs on a single thread, treats the agents' execution cycle (see agents below) as atomic and inteprets the agents in the environment serially. Concurrency has been supported in previous iterations of the GOLEM framework and is planned for the next major version(s) of PyStarWorlds.

## Agents

PyStarWorlds interleaves environment and agent execution in a round-robin fashion. At each time step each agent runs a <i> perceive-revise-decide-execute</i> cycle returning an action according to a given top level goal, determining the agent’s behaviour. Given this agent cycle, a developer is free to specify these methods, according to the needs of the application.

To aid the agent development, we recommend that the behaviour for each agent to be conceptualised with <a href="https://teleoreactiveprograms.net/">teleo-reactive programs</a> of the form:

<i>Goal:{Conditions<sub>1</sub> &rarr; Action<sub>1</sub>, ..., Conditions<sub>n</sub> &rarr; Action<sub>n</sub>}</i>,

where an <i>Action<sub>i</sub></i> is either atomic or a <i>SubGoal</i> specified with further condition action rules. These behaviours are translated as Python methods, checking the current observations and the agent state to pursue the most appropriate agent intention at each time step in a dynamic manner.

<img align="right" src="docs/agent.png">

# Related Projects

- [ICUA](https://github.com/dicelab-rhul/ICUA)
- [Vacuum World](https://github.com/dicelab-rhul/vacuumworld) 
- [pyteleor](https://github.com/BenedictWilkins/pyteleor/tree/master/pyteleor)
