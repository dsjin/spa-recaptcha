<template>
  <div>
    <re-captcha
      :siteKey="'own-recapcha-sitekey'"
      @verify="verify"
      @expired-callback="expiredCallback"
      @error-callback="errorCallback"
      ref="recaptcha"
    />
    <button
      @click="invoke"
    >
      Invoke The Challenge
    </button>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import ReCaptcha from '@/components/ReCaptcha.vue'
export default Vue.extend({
  name: 'SendForm',
  components: {
    ReCaptcha
  },
  methods: {
    verify (response: any) {
      console.log(response)
    },
    expiredCallback () {
      console.log('expiredCallback')
    },
    errorCallback () {
      console.log('errorCallback')
    },
    invoke () {
      (this.$refs.recaptcha as any).execute()
    }
  }
})
</script>

<style>
</style>
