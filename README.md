# WordleAI
A Python script meant to solve the popular game wordle, running a simulation for every valid word using a variety of increasingly effective methods. 

![wordleRules](https://github.com/eharris733/WordleAI/assets/65927291/4efd5c3e-66ec-4631-8e8a-a2902565eead)

## Methods
Three implemented algorithms
1. A random guesser, that just guesses random valid words based on uncovered restraints.
2. A popularity guesser, that guesses words that contain an overall highest popularity score, in other words, have the most commonly used letters in combination with each other
3. A heuristic guesser, which simulates guessing a word, and then counts how many possible guesses it eliminates. This is by far the slowest (and causes the program to take up to ten minutes of running time), but also by far the most effective. 

## Project Status
This project is by all means complete, it was accepted by the Bard CS program as a means to "moderate" (or fully declare) into the major of computer science. However, there is definitely room for improvement. One easy fix is that a specific Wordle edge case is mishandled. Currently, the behavior for if two identical letters appear in the same word (i.e. sheep), the second e should also be yellow or green, however, this program does not assume that this is the case. Another factor is that there are definitely other clever algorithms that utilize heuristics to eliminate possible words in a more precise manner. This program assumes playing on "hard mode" where guesses that violate previous constraints (i.e., green 'y' means all subsequent words must contain a y in that slot), but that is not the preferred method for most Wordle players, and certainly not the most optimal way of solving wordle. 

## Project Details
Suppose you are curious about the workings of this project. In that case, I have written a report on both the rules of Wordle and the various considerations of my code, including but not limited to 
the algorithms, run time, and space complexity, as well as a brief overview of other literature on the topic. 
https://docs.google.com/document/d/12Z4gfX2THa1DHv4k4rO9ZbR2e2EXrmDXtEHB2RwN4Ns/edit?usp=sharing 
