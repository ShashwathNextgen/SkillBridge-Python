class BookDAO():
	def __init__(self, DAO):
		self.db = DAO
		self.db.table = "books"

	def delete(self, id):
		q = self.db.query("DELETE FROM @table where id={}".format(id))
		self.db.commit()

		return q


	def reserve(self, user_id, book_id):
		if not self.available(book_id):
			return "err_out"

		q = self.db.query("INSERT INTO reserve (user_id, book_id) VALUES('{}', '{}');".format(user_id, book_id))

		self.db.query("UPDATE @table set count=count-1 where id={};".format(book_id))
		self.db.commit()

		return q

	def getBooksByUser(self, user_id):
		q = self.db.query("select * from @table left join reserve on reserve.book_id = @table.id where reserve.user_id={}".format(user_id))

		books = q.fetchall()

		print(books)
		return books

	def getBooksCountByUser(self, user_id):
		q = self.db.query("select count(reserve.book_id) as books_count from @table left join reserve on reserve.book_id = @table.id where reserve.user_id={}".format(user_id))

		books = q.fetchall()

		print(books)
		return books

	def getBook(self, id):
		q = self.db.query("select * from @table where id={}".format(id))

		book = q.fetchone()

		print(book)
		return book

	def available(self, id):
		book = self.getById(id)
		count = book[6]

		if count < 1:
			return False

		return True

	def getById(self, id):
		q = self.db.query("select * from @table where id='{}'".format(id))

		book = q.fetchone()

		return book

	def list(self, availability=True):
		query="select * from @table"
		# Usually when no-admin user query for book
		if availability==1: query= query+"  WHERE availability={}".format(availability)
		
		books = self.db.query(query)
		
		books = books.fetchall()


		return books

	def getReservedBooksByUser(self, user_id):
		query = f"SELECT string_agg(book_id::text, ',') AS user_books FROM reserve WHERE user_id={user_id}"
		books = self.db.query(query)
		result = books.fetchone()
		return {'user_books': result[0]} if result else {'user_books': ''}

	def search_book(self, name, availability=True):
		query="select * from @table where name LIKE '%{}%'".format(name)

		# Usually when no-admin user query for book
		if availability==1: query= query+"  AND availability={}".format(availability)

		q = self.db.query(query)
		books = q.fetchall()
		
		return books



