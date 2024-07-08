from yoomoney import Quickpay


async def pay_func(label):
    """Создание ссылки на форму оплаты"""

    quickpay = Quickpay(
                receiver="4100118742752795",
                quickpay_form="shop",
                targets="Sponsor this project",
                paymentType="SB",
                sum=10,
                label=label
                )

    return quickpay.base_url
