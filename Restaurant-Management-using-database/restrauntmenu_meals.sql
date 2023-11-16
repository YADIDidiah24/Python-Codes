-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: restrauntmenu
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `meals`
--

DROP TABLE IF EXISTS `meals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `meals` (
  `meal_id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `ingredients` text,
  PRIMARY KEY (`meal_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meals`
--

LOCK TABLES `meals` WRITE;
/*!40000 ALTER TABLE `meals` DISABLE KEYS */;
INSERT INTO `meals` VALUES (1,'Club Sandwich',10.99,'sandwich','Bread, Turkey, Bacon, Lettuce, Tomato, Mayonnaise'),(2,'Caesar Salad',8.99,'salad','Romaine Lettuce, Parmesan Cheese, Croutons, Caesar Dressing'),(3,'Grilled Chicken Sandwich',12.99,'sandwich','Grilled Chicken Breast, Lettuce, Tomato, Onion, Pickles, Mustard, Mayonnaise'),(4,'Spaghetti Bolognese',14.99,'entree','Spaghetti, Ground Beef, Tomato Sauce, Garlic, Onion, Basil, Parmesan Cheese'),(5,'Margherita Pizza',9.99,'entree','Pizza Dough, Tomato Sauce, Mozzarella Cheese, Basil'),(6,'BBQ Chicken Pizza',12.99,'entree','Pizza Dough, BBQ Sauce, Grilled Chicken, Red Onion, Mozzarella Cheese, Cilantro'),(7,'Roast Beef Sandwich',11.99,'sandwich','Roast Beef, Swiss Cheese, Horseradish Sauce, Lettuce, Tomato, Onion, Rye Bread'),(8,'Veggie Burger',9.99,'sandwich','Veggie Patty, Lettuce, Tomato, Onion, Pickles, Ketchup, Mustard'),(9,'Fish and Chips',13.99,'entree','Beer-Battered Cod, French Fries, Tartar Sauce'),(10,'Chicken Caesar Salad',8.99,'salad','Romaine Lettuce, Grilled Chicken Breast, Parmesan Cheese, Croutons, Caesar Dressing'),(11,'Philly Cheesesteak',10.99,'sandwich','Beef Sirloin, Green Peppers, Onions, Provolone Cheese, Hoagie Roll'),(12,'Chicken Alfredo',12.99,'pasta','Fettuccine Pasta, Chicken Breast, Heavy Cream, Parmesan Cheese'),(14,'Beef Tacos',9.99,'tacos','Ground Beef, Taco Seasoning Mix, Shredded Lettuce, Diced Tomatoes'),(15,'Grilled Cheese Sandwich',5.99,'sandwich','Bread Slices, American Cheese Slices'),(16,'Virgin Margarita',5.99,'drink','Lime Juice, Orange Juice, Agave Nectar'),(17,'Spaghetti and Meatballs',11.99,'pasta','Spaghetti Pasta,Napolitan Sauce,Garlic Meatballs'),(18,'Virgin Mojito',6.99,'drink','Lime Juice, Mint Leaves, Club Soda'),(19,'Virgin Pina Colada',7.99,'drink','Pineapple Juice,Cream of Coconut'),(20,'Lemonade',3.99,'drink','Lemon Juice, Sugar, Water, Ice'),(21,'Orange Juice',2.99,'drink','Orange Juice, Water, Ice'),(22,'Iced Tea',3.00,'drink','Black Tea, Sugar, Water, Ice'),(23,'Soda',1.99,'drink','Carbonated Water, High Fructose Corn Syrup, Phosphoric Acid, Natural Flavors, Caffeine'),(24,'Tuna Salad Sandwich',8.99,'sandwich','Tuna, Mayonnaise, Celery, Red Onion, Lettuce, Tomato, Bread'),(25,'BLT Sandwich',9.99,'sandwich','Bacon, Lettuce, Tomato, Mayonnaise, Bread'),(26,'Veggie Delight',9.99,'sandwich','Whole Wheat Bread, Hummus, Avocado, Cucumber, Tomato, Lettuce'),(27,'Caprese Sandwich',8.99,'sandwich','Ciabatta Bread, Fresh Mozzarella, Tomato, Basil, Balsamic Vinegar, Olive Oil'),(28,'Falafel Sandwich',10.99,'sandwich','Pita Bread, Falafel Balls, Hummus, Tomato, Cucumber, Pickles, Tahini Sauce'),(29,'Egg Salad Sandwich',8.99,'sandwich','White Bread, Hard-Boiled Eggs, Mayonnaise, Mustard, Onion, Celery'),(30,'Roasted Veggie Panini',11.99,'sandwich','Focaccia Bread, Roasted Red Peppers, Zucchini, Eggplant, Mozzarella Cheese, Pesto'),(31,'Portobello Mushroom Sandwich',12.99,'sandwich','Whole Wheat Bun, Grilled Portobello Mushroom, Tomato, Arugula, Balsamic Glaze'),(32,'Veggie Wrap',8.99,'sandwich','Whole Wheat Wrap, Hummus, Lettuce, Tomato, Cucumber, Carrots'),(33,'shawarma',5.00,'sandwich','kubus, Hummus, Lettuce, fries, Cucumber, chicken '),(34,'chicken briyani',8.99,'entree','rice chicken tomatoes yourt gingergarlicpaste greenchilipeppers');
/*!40000 ALTER TABLE `meals` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-27 21:41:15
