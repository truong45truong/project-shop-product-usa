<template>
    <div class="container mt-5 flash-sale-top">
        <div class="row m-3 py-5 flash-sale-inside">
            <div class="col-sm-6 d-flex align-items-center ">
                <font-awesome-icon icon="fa-solid fa-bolt" class="text-white fs-3 me-2" />
                <h3 class="text-white m-0 me-1 text-flash-sale">Flash Sale:</h3>
            </div>
            <div class="col-sm-6 mb-2 d-flex align-items-center justify-content-end mt-2 ">
              <CountDownFLashSale :date_prop="date_flash_sale" :hour_prop="hour_flash_sale" :mins_prop="mins_flash_sale" :secs_prop="secs_flash_sale"/>
            </div>
        </div>  
        <div class="row m-0 ">
            <Carousel :settings="settings" :breakpoints="breakpoints" :wrap-around="true">
                <Slide v-for="item in listProductItem" :key="item" :class="'mx-1 shawdo'" >
                    <product-item :slug="item.slug" :photo="item.data" :name="item.name" :sale="item.sale"
                        :price="item.price" :status="item.status_heart" :hearts="item.count_heart"
                    />
                </Slide>
            
                <template #addons>
                    <Pagination />
                    <Navigation class= "pagination-container" />
                </template>
            </Carousel>
        </div>
    </div>
</template>
  
<script>
import { Carousel, Navigation, Slide, Pagination } from 'vue3-carousel'
import { ProductApiService } from '../../common/product.service'
import CountDownFLashSale from '../../components/other/CountDowmFLashSale.vue'
import ProductItem from '../../components/product/ProductItem.vue'
import 'vue3-carousel/dist/carousel.css'
import 'vue3-carousel/dist/carousel.js'
export default ({
    name: 'ListProductItem',
    components: {
        ProductItem,
        Pagination,
        Carousel,
        Slide,
        Navigation,
        CountDownFLashSale
    },
    data: () => ({
        listProductItem : [],
        date_flash_sale : false,
        hour_flash_sale : false,
        mins_flash_sale : false,
        secs_flash_sale : false,
        settings: {
        itemsToShow: 2,
        snapAlign: 'center',
      },
      // breakpoints are mobile first
      // any settings not specified will fallback to the carousel settings
      breakpoints: {
        400: {
          itemsToShow: 2,
          snapAlign: 'center',
        },
        // 700px and up
        700: {
          itemsToShow: 3,
          snapAlign: 'center',
        },
        // 1024 and up
        1024: {
          itemsToShow: 4,
          snapAlign: 'center',
        },
      },
    }),
    methods :{
      async changeStatusHeartProduct(){
            await ProductApiService.get().then(res => {
                console.log(res)
                this.listProductItem = Array.from(res.data.products)
            })
        }
    },
    async created(){
        await ProductApiService.get().then(res => {
          for( let item of res.data.products){
            if(item.sale > 0){
              this.listProductItem.push(item)
            }
          }
           
        })
        this.date_flash_sale = 3;
        this.hour_flash_sale = 17;
        this.mins_flash_sale = 30;
        this.secs_flash_sale = 60;
    }
})
</script>
<style>
.box-demo {
    height:85%;
    position:relative;
    overflow:hidden
}
.flash-sale-inside {
    background-color: rgb(36,41,47);
}



/* CSS */
.flash-sale-top {
  --b: 3px;   /* border thickness */
  --s: 1em; /* size of the corner */
  --color: #373B44;
  
  padding: calc(.5em + var(--s)) calc(.9em + var(--s));
  color: var(--color);
  --_p: var(--s);
  background:
    conic-gradient(from 90deg at var(--b) var(--b),#0000 90deg,var(--color) 0)
    var(--_p) var(--_p)/calc(100% - var(--b) - 2*var(--_p)) calc(100% - var(--b) - 2*var(--_p));
  transition: .3s linear, color 0s, background-color 0s;
  outline: var(--b) solid #0000;
  outline-offset: .6em;
  font-size: 16px;

  border: 0;

  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.flash-sale-top:hover,
.flash-sale-top:focus-visible{
  --_p: 0px;
  outline-color: var(--color);
  outline-offset: .05em;
}

.show-all-product-flash-sale{
    font-family: 'Sassy Frass', cursive;
    font-weight: 700;
}

.pagination-container {
  background-color: rgb(36,41,47);
  padding: 10px;
  margin-top: 10px;
}
.carousel__icon{
  color:white;
}
.carousel__icon path{
  color:white;
  font-size: larger;
}
.carousel__prev,
.carousel__next {
  background-color: rgb(36,41,47);
  color: white;
  font-size: 14px;
  padding: 2px 4px;
  border: 1px solid rgb(36,41,47);
  border-radius: 5px;
  margin-right: 8px;
  border-radius: 50%;
}
@media only screen and (max-width: 1024px)
{


}
@media only screen and (max-width: 768px)
{

}
@media only screen and (max-width: 524px){
  .flash-sale-top {
    border:none;

  }
  .flash-sale-top:hover,
  .flash-sale-top:focus-visible{
    --_p: var(--s);
    outline: var(--b) solid #0000;
    outline-offset: .6em;
  }
}
@media only screen and (max-width: 424px)
{   
    .flash-sale-inside {
      padding : 10px 10% !important;
    }
    .text-flash-sale {
      font-size: 18px ;
    }
    .carousel__prev,
    .carousel__next {
      display:none;
    }
}
</style>