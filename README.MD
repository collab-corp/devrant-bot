This project will hopefully result in a simple natural language enhancement on the naive bayesian classifier that both improves response accuracy as well as decreasing search time for large datasets.

The basic plan is to implement sentence diagramming (something i never learned in school but have since come to think of as 'generally a good idea') in order to find root words within a sentence to help identify what the subject of the conversation is before then using an NBC to locate a response within a much smaller, much more dedicated corpus.

The slowdown with this approach will be that at first it will be hard if not impossible for machine learning to improve upon the classification until the first dataset and training/validation set is completed by a real human, this will occur for each language introduced and is better served by maintaining separate corpii for each language.
