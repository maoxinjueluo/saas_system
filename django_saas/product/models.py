# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comment(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    store_category_id = models.PositiveIntegerField()
    goods_id = models.PositiveIntegerField()
    comment_data = models.TextField(blank=True, null=True)
    image_src = models.CharField(max_length=1000)
    is_hide = models.IntegerField()
    star_rating = models.PositiveIntegerField()
    comment_tag = models.CharField(max_length=255)
    is_checked = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comment'


class CommentTag(models.Model):
    mch_id = models.PositiveIntegerField()
    star_rating = models.PositiveIntegerField()
    tag_data = models.CharField(max_length=30)
    state = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comment_tag'


class GoodsCategory(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    title = models.CharField(max_length=20)
    is_show = models.PositiveIntegerField()
    app_show = models.PositiveIntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_category'


class GoodsConsume(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    category_id = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    image_src = models.CharField(max_length=1000)
    describe = models.CharField(max_length=255)
    bar_code = models.CharField(max_length=30)
    unit_id = models.PositiveIntegerField()
    specs = models.CharField(max_length=20)
    type = models.PositiveIntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    quality_day = models.PositiveSmallIntegerField()
    state = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_consume'


class GoodsConsumeBottleUnitConver(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    consume_id = models.PositiveIntegerField()
    unit_id = models.PositiveIntegerField()
    min_conver_number = models.PositiveIntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_consume_bottle_unit_conver'
        unique_together = (('mch_id', 'store_id', 'consume_id', 'unit_id', 'state'),)


class GoodsConsumeUnitConvert(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    consume_id = models.PositiveIntegerField()
    unit_id = models.PositiveIntegerField()
    conver_number = models.PositiveIntegerField()
    is_min = models.PositiveIntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_consume_unit_convert'
        unique_together = (('mch_id', 'store_id', 'consume_id', 'unit_id', 'state'),)


class GoodsInvestCard(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    image_src = models.CharField(max_length=1000)
    type = models.PositiveIntegerField()
    money = models.DecimalField(max_digits=10, decimal_places=2)
    give_money = models.DecimalField(max_digits=10, decimal_places=2)
    give_expire_type = models.PositiveIntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_invest_card'
        unique_together = (('mch_id', 'store_id', 'state'),)


class GoodsPackage(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    category_id = models.PositiveIntegerField()
    describe = models.CharField(max_length=255)
    origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_src = models.CharField(max_length=100)
    option_count = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    services = models.TextField(blank=True, null=True)
    effective_day = models.PositiveIntegerField()
    effective_type = models.IntegerField()
    sort = models.PositiveIntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_package'


class GoodsPackageNotStandard(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    category_id = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    describe = models.CharField(max_length=255)
    origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_src = models.CharField(max_length=1000)
    option_count = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    services = models.TextField(blank=True, null=True)
    effective_type = models.IntegerField()
    effective_day = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    create_staff_id = models.PositiveIntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_package_not_standard'


class GoodsProduct(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    category_id = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    bar_code = models.CharField(max_length=30)
    unit_id = models.PositiveIntegerField()
    specs = models.CharField(max_length=20)
    image_src = models.CharField(max_length=1000)
    origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.PositiveIntegerField()
    quality_day = models.PositiveSmallIntegerField()
    content = models.TextField(blank=True, null=True)
    all_store_display = models.PositiveIntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_product'


class GoodsProductDisplay(models.Model):
    product_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_product_display'
        unique_together = (('product_id', 'store_id'),)


class GoodsProductUnitConvert(models.Model):
    product_id = models.PositiveIntegerField()
    unit_id = models.PositiveIntegerField()
    conver_number = models.PositiveIntegerField()
    is_min = models.PositiveIntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_product_unit_convert'


class GoodsService(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    category_id = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    describe = models.CharField(max_length=255)
    duration = models.PositiveSmallIntegerField()
    origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sort = models.PositiveIntegerField()
    image_src = models.CharField(max_length=1000)
    content = models.TextField(blank=True, null=True)
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_service'
        unique_together = (('mch_id', 'store_id', 'category_id', 'state'),)


class GoodsServiceConsumeInfo(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    service_id = models.PositiveIntegerField()
    consume_id = models.PositiveIntegerField()
    consume_type = models.PositiveIntegerField()
    consume_num = models.PositiveIntegerField()
    unit_id = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_service_consume_info'


class GoodsServiceNotStandard(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    category_id = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    describe = models.CharField(max_length=255)
    duration = models.PositiveSmallIntegerField()
    origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sort = models.PositiveIntegerField()
    image_src = models.CharField(max_length=100)
    nav_images = models.CharField(max_length=1000)
    create_staff_id = models.PositiveIntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_service_not_standard'


class GoodsStoreConsume(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    consume_id = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    store_category_id = models.PositiveIntegerField()
    store_cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_num = models.IntegerField()
    state = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_store_consume'


class GoodsStoreInvestCard(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    invest_card_id = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_store_invest_card'
        unique_together = (('mch_id', 'store_id', 'invest_card_id', 'state'),)


class GoodsStorePackage(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    package_id = models.PositiveIntegerField()
    is_standard = models.PositiveIntegerField()
    store_category_id = models.PositiveIntegerField()
    store_origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    store_price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_store_package'
        unique_together = (('mch_id', 'store_id', 'package_id', 'is_standard', 'state'),)


class GoodsStorePackageLimitBuy(models.Model):
    store_package_id = models.PositiveIntegerField()
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    package_id = models.PositiveIntegerField()
    is_standard = models.PositiveIntegerField()
    limit_buy_num = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_store_package_limit_buy'
        unique_together = (('mch_id', 'store_id', 'package_id', 'is_standard', 'state'),)


class GoodsStorePackageShow(models.Model):
    store_package_id = models.PositiveIntegerField()
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    package_id = models.PositiveIntegerField()
    is_standard = models.PositiveIntegerField()
    is_show = models.PositiveIntegerField()
    app_show = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_store_package_show'
        unique_together = (('mch_id', 'store_id', 'package_id', 'is_standard', 'state'),)


class GoodsStoreProduct(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    store_category_id = models.PositiveIntegerField()
    store_origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    store_price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_store_product'
        unique_together = (('mch_id', 'store_id', 'product_id', 'state'),)


class GoodsStoreProductLimitBuy(models.Model):
    store_product_id = models.PositiveIntegerField()
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    limit_buy_num = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_store_product_limit_buy'
        unique_together = (('mch_id', 'store_id', 'product_id', 'state'),)


class GoodsStoreProductShow(models.Model):
    store_product_id = models.PositiveIntegerField()
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    is_show = models.PositiveIntegerField()
    app_show = models.PositiveIntegerField()
    state = models.IntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_store_product_show'
        unique_together = (('mch_id', 'store_id', 'product_id', 'state'),)


class GoodsStoreService(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    service_id = models.PositiveIntegerField()
    is_standard = models.PositiveIntegerField()
    store_category_id = models.PositiveIntegerField()
    store_origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    store_price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_store_service'
        unique_together = (('mch_id', 'store_id', 'service_id', 'is_standard', 'state'),)


class GoodsStoreServiceLimitBuy(models.Model):
    store_service_id = models.PositiveIntegerField()
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    service_id = models.PositiveIntegerField()
    is_standard = models.PositiveIntegerField()
    limit_buy_num = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_store_service_limit_buy'
        unique_together = (('mch_id', 'store_id', 'service_id', 'is_standard', 'state'),)


class GoodsStoreServiceShow(models.Model):
    store_service_id = models.PositiveIntegerField()
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    service_id = models.PositiveIntegerField()
    is_standard = models.PositiveIntegerField()
    is_show = models.PositiveIntegerField()
    app_show = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_store_service_show'
        unique_together = (('mch_id', 'store_id', 'service_id', 'is_standard', 'state'),)


class GoodsUnit(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    unit = models.CharField(max_length=5)
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_unit'
        unique_together = (('mch_id', 'store_id', 'unit', 'state'),)


class OrderMaster(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    staff_id = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    type = models.PositiveIntegerField()
    remark = models.CharField(max_length=100)
    origin = models.PositiveIntegerField()
    total_origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_id = models.PositiveIntegerField()
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2)
    change_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_pre_amount = models.DecimalField(max_digits=10, decimal_places=2)
    member_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_should_receive = models.DecimalField(max_digits=10, decimal_places=2)
    total_real_receive = models.DecimalField(max_digits=10, decimal_places=2)
    pay_method = models.PositiveIntegerField()
    is_batch_pay = models.IntegerField()
    order_code = models.IntegerField()
    comment_code = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_master'


class OrderPackage(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    master_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    package_id = models.PositiveIntegerField()
    staff_id = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    remark = models.CharField(max_length=100)
    image_src = models.CharField(max_length=100)
    package_term = models.DateTimeField()
    origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    scribing_price = models.DecimalField(max_digits=10, decimal_places=2)
    member_price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_id = models.PositiveIntegerField()
    change_price = models.DecimalField(max_digits=10, decimal_places=2)
    pre_amount = models.DecimalField(max_digits=10, decimal_places=2)
    should_receive = models.DecimalField(max_digits=10, decimal_places=2)
    real_receive = models.DecimalField(max_digits=10, decimal_places=2)
    pay_method = models.PositiveIntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_package'


class OrderProduct(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    master_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    staff_id = models.PositiveIntegerField()
    store_category_id = models.PositiveIntegerField()
    priduct_id = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    image_src = models.CharField(max_length=100)
    pick_up_code = models.CharField(max_length=30)
    stock_id = models.PositiveIntegerField()
    remark = models.CharField(max_length=100)
    origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    scribing_price = models.DecimalField(max_digits=10, decimal_places=2)
    member_price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_id = models.PositiveIntegerField()
    change_price = models.DecimalField(max_digits=10, decimal_places=2)
    pre_amount = models.DecimalField(max_digits=10, decimal_places=2)
    unit_should_receive = models.DecimalField(max_digits=10, decimal_places=2)
    should_receive = models.DecimalField(max_digits=10, decimal_places=2)
    real_receive = models.DecimalField(max_digits=10, decimal_places=2)
    pay_method = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_product'


class OrderRevestCard(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    master_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    card_id = models.PositiveIntegerField()
    staff_id = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    card_money = models.DecimalField(max_digits=10, decimal_places=2)
    give_money = models.DecimalField(max_digits=10, decimal_places=2)
    give_term = models.DateTimeField()
    origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    scribing_price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_id = models.PositiveIntegerField()
    change_price = models.DecimalField(max_digits=10, decimal_places=2)
    pre_amount = models.DecimalField(max_digits=10, decimal_places=2)
    should_receive = models.DecimalField(max_digits=10, decimal_places=2)
    real_receive = models.DecimalField(max_digits=10, decimal_places=2)
    pay_method = models.PositiveIntegerField()
    give_used_money = models.DecimalField(max_digits=10, decimal_places=2)
    give_over_money = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_revest_card'


class OrderService(models.Model):
    mch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    master_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    staff_id = models.PositiveIntegerField()
    service_id = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    image_src = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    scribing_price = models.DecimalField(max_digits=10, decimal_places=2)
    member_price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_id = models.PositiveIntegerField()
    change_price = models.DecimalField(max_digits=10, decimal_places=2)
    pre_amount = models.DecimalField(max_digits=10, decimal_places=2)
    should_receive = models.DecimalField(max_digits=10, decimal_places=2)
    real_receive = models.DecimalField(max_digits=10, decimal_places=2)
    pay_method = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_service'


class SdkLtv(models.Model):
    pay_type = models.PositiveIntegerField()
    register_time = models.DateField()
    incr_amt = models.PositiveIntegerField()
    day1 = models.BigIntegerField()
    day2 = models.BigIntegerField()
    day3 = models.BigIntegerField()
    day4 = models.BigIntegerField()
    day5 = models.BigIntegerField()
    day6 = models.BigIntegerField()
    day7 = models.BigIntegerField()
    day8 = models.BigIntegerField()
    day9 = models.BigIntegerField()
    day10 = models.BigIntegerField()
    day11 = models.BigIntegerField()
    day12 = models.BigIntegerField()
    day13 = models.BigIntegerField()
    day14 = models.BigIntegerField()
    day15 = models.BigIntegerField()
    day16 = models.BigIntegerField()
    day17 = models.BigIntegerField()
    day18 = models.BigIntegerField()
    day19 = models.BigIntegerField()
    day20 = models.BigIntegerField()
    day21 = models.BigIntegerField()
    day22 = models.BigIntegerField()
    day23 = models.BigIntegerField()
    day24 = models.BigIntegerField()
    day25 = models.BigIntegerField()
    day26 = models.BigIntegerField()
    day27 = models.BigIntegerField()
    day28 = models.BigIntegerField()
    day29 = models.BigIntegerField()
    day30 = models.BigIntegerField()
    count_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sdk_ltv'
        unique_together = (('pay_type', 'register_time'),)
