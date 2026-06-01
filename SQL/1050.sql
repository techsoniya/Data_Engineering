-- 1050. Actors and Directors Who Cooperated At Least Three Times
-- Solved

-- SQL Schema

-- Table: ActorDirector

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | actor_id    | int     |
-- | director_id | int     |
-- | timestamp   | int     |
-- +-------------+---------+
-- timestamp is the primary key (column with unique values) for this table.
 

-- Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

-- Return the result table in any order.

-- The result format is in the following example.

-- Example 1:

-- Input: 
-- ActorDirector table:
-- +-------------+-------------+-------------+
-- | actor_id    | director_id | timestamp   |
-- +-------------+-------------+-------------+
-- | 1           | 1           | 0           |
-- | 1           | 1           | 1           |
-- | 1           | 1           | 2           |
-- | 1           | 2           | 3           |
-- | 1           | 2           | 4           |
-- | 2           | 1           | 5           |
-- | 2           | 1           | 6           |
-- +-------------+-------------+-------------+
-- Output: 
-- +-------------+-------------+
-- | actor_id    | director_id |
-- +-------------+-------------+
-- | 1           | 1           |
-- +-------------+-------------+
-- Explanation: The only pair is (1, 1) where they cooperated exactly 3 times.

--------------------------------------------------------------------------------------------------------------------------------------------
--Optimized solution with HAVING clause
-- # Write your MySQL query statement below

SELECT actor_id,
       director_id
FROM ActorDirector
GROUP BY   actor_id, 
           director_id
HAVING COUNT(*)>=3;



-- # Write your MySQL query statement below
--using subquery to count the number of times each pair (actor_id, director_id) cooperated and then filter those pairs with at least 3 cooperations

SELECT 
actor_id,
director_id
FROM
    (   
    SELECT 
        actor_id,
        director_id,
        COUNT(*) AS Times
    FROM ActorDirector
    GROUP BY    actor_id, 
                director_id
) AS t
WHERE Times>=3;
