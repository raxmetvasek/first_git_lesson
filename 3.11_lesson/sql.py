import json
from sqlalchemy import create_engine, ForeignKey, String, Float, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

with open('catalog.json', 'r', encoding = 'utf-8') as file:
	products_data = json.load(file)
	
DATABASE_URL = 'sqlite://online_shop.db'
engine = create_engine(DATABASE_URL, echo = False)
Session = sessionmaker(bind = engine)

class Base(DeclarativeBase):
	pass

class Category(Base):
	__tablename__ = 'categories'

	id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True) 
	name: Mapped[str] = mapped_column(String, unique=True, nullable = False)
	description: Mapped[float] = mapped_column(Float, nullable=False)
	category_id: Mapped[int | None] = mapped_column(ForeignKey('categories.id', ondelete = 'SET NULL')) 
Base.metadata.create_all(engine)
with Session() as session:
	category_cache = {}
	for item in product_data:
		cat_info = item['category']
		cat_name = cat_info['name']
		cat_desc = cat_info['description']
		if cat_name not in category_cache:
			stmt = select(Category).where(Category.name == cat_name) 
			category_obj = session.scalars(stmt).first()
			if not category_obj:
				category_obj = Category(name = cat_name, description = cat_desc)
				session.add(category_obj)
				session.flush()
			category_cache[cat_name] = category_obj
		else:
			category_obj = category_cache[cat_name]
		new_product = Product (
			product_name = item['product_name'],
			price = item['price'],
			category_id = category_obj.id
		)
		session.commit()
print('данные успешно сохранены')

