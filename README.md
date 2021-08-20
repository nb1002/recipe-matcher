# recipe-matcher

**Purpose**
The target audience for this website is beginners or amateur cooks who are looking to find recipes for easy and quick meals to make with little ingredients. Recipes from various sources/cultures will be used, allowing users to expand their palates. Currently similar types of websites exist, i.e myfridgefood.com, recipeland.com, realfood.tesco.com etc (in english). However, there is a market for 
a recipe matching website in non-english languages (ie mongolian). Initial test website will be developed in english but will later be translated, giving users the option to pick between languages.  The database will be minimal to start with, only including 5-7 entries for each attributes. 

**Functionalities**
-Users will be able to enter ingredients to the input field for a recipe that matches their ingredients
-Input field will have a dropdown ingredients list when user types. minimum 3 letters to be written before menu is activated
-When submit button is clicked the query will be run to retrieve matching recipes
-Recipes to be displayed will contain image of the meal, ingredients list, link to the recipe, and serving/cook time.
-Menu bar/buttons will have search bar, recipes, and login options.
-Mock up is developed to show the overall look of the website but will be improved during development. 
-Users can sign up and login to save recipes. 
-Submission for recipes by users to be added in future.
  
Rough mock ups:
https://imgur.com/a/oIYZeXj

**ERD & Schema**
-User (UserID, UserName, UserEmail, UserPassword)
-Recipes (RecipeID, Name, Ingredients, Type, Serving, Time, Img, Directions)
-Ingredients (IngredientID, Name, Counter)
-IngInRecipe (IngredientID, RecipeID)
-UserFavorites(UserID, RecipeID)
-Type (Type, Description) 
-RecipeType (Type, RecipeID

ERD
https://imgur.com/a/9XpYHsO

Detailed Schema
-Recipes will have id, name, serving, time, ingredients list, directions, image and recipe type. 
-Users sign up for an account to be able to save or favorite recipes. email, password and name will be recorded. Users will be assigned id. 
-Ingredients will have ingredients id, name and counter. Counter will be used to determine which ingredients are the most popular.  	
-IngInRecipe is a weak entity containing ingredientID and recipeID. It is to see which ingredient is used in what recipe. Amount used of each will also be recorded. 
-Type will have recipe type i.e vegan, gluten free, vegetarian, dairy free etc. Has Type and Description columns. (to be added later)
-RecipeType is a weak entity, containing type and recipe id. Type will be assigned to each recipe according to its id. A recipe can have many types.  (to be added later)
