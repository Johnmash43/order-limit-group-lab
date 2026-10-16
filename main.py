import sqlite3


def read_sql(query, connection):
    """Run a query and return its rows without an external dependency."""
    return connection.execute(query).fetchall()

# ==========================================
# Part 1: Basic Filtering (planets.db)
# ==========================================
conn1 = sqlite3.connect("planets.db")

# 1. Return all the columns for planets that have 0 moons.
planets_zero_moons = read_sql(
    """
    SELECT * 
    FROM planets 
    WHERE moons = 0;
""",
    conn1,
)

# 2. Return the name and mass of each planet that has a name with exactly 7 letters.
planets_seven_letters = read_sql(
    """
    SELECT name, mass 
    FROM planets 
    WHERE LENGTH(name) = 7;
""",
    conn1,
)


# ==========================================
# Part 2: Advanced Filtering (planets.db)
# ==========================================

# 1. Return the name and mass for each planet that has a mass <= 1.00.
planets_mass_low = read_sql(
    """
    SELECT name, mass 
    FROM planets 
    WHERE mass <= 1.00;
""",
    conn1,
)

# 2. Return all columns for planets with at least one moon and mass < 1.00.
planets_moon_mass = read_sql(
    """
    SELECT * 
    FROM planets 
    WHERE moons > 0 AND mass < 1.00;
""",
    conn1,
)

# 3. Return the name and color of planets that have a color containing "blue".
planets_blue = read_sql(
    """
    SELECT name, color 
    FROM planets 
    WHERE color LIKE '%blue%';
""",
    conn1,
)


# ==========================================
# Part 3: Ordering and Limiting (dogs.db)
# ==========================================
conn2 = sqlite3.connect("dogs.db")

# 1. Hungry dogs sorted from youngest to oldest.
hungry_youngest = read_sql(
    """
    SELECT name, age, breed 
    FROM dogs 
    WHERE hungry = 1 
    ORDER BY age ASC;
""",
    conn2,
)

# 2. Hungry dogs between ages 2 and 7, sorted alphabetically by name.
hungry_two_to_seven = read_sql(
    """
    SELECT name, age, hungry 
    FROM dogs 
    WHERE hungry = 1 AND age BETWEEN 2 AND 7 
    ORDER BY name ASC;
""",
    conn2,
)

# 3. 4 oldest dogs, sorted alphabetically based on the breed.
oldest_four_dogs = read_sql(
    """
    SELECT name, age, breed 
    FROM (
        SELECT name, age, breed 
        FROM dogs 
        ORDER BY age DESC 
        LIMIT 4
    ) 
    ORDER BY breed ASC;
""",
    conn2,
)


# ==========================================
# Part 4: Aggregation (babe_ruth.db)
# ==========================================
conn3 = sqlite3.connect("babe_ruth.db")

# 1. Total number of years Babe Ruth played professional baseball.
total_years = read_sql(
    """
    SELECT COUNT(*) AS total_years 
    FROM babe_ruth_stats;
""",
    conn3,
)

# 2. Total number of home runs hit by Babe Ruth during his career.
total_home_runs = read_sql(
    """
    SELECT SUM(HR) AS total_home_runs 
    FROM babe_ruth_stats;
""",
    conn3,
)


# ==========================================
# Part 5: Grouping and Aggregation (babe_ruth.db)
# ==========================================

# 1. Team name and number of years played, aliased as number_years.
team_years = read_sql(
    """
    SELECT team, COUNT(*) AS number_years 
    FROM babe_ruth_stats 
    GROUP BY team;
""",
    conn3,
)

# 2. Team name and average at-bats (> 200), aliased as average_at_bats.
team_avg_at_bats = read_sql(
    """
    SELECT team, AVG(AB) AS average_at_bats 
    FROM babe_ruth_stats 
    GROUP BY team 
    HAVING AVG(AB) > 200;
""",
    conn3,
)


# ==========================================
# Close all database connections
# ==========================================
conn1.close()
conn2.close()
conn3.close()
print("All queries executed successfully and connections closed.")